from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

import requests
import json
from .serializers import SearchResultSerializer
from .models import Search, SearchResult


class SearchViewSet(viewsets.ViewSet):
    '''
        viewset that provides custom action to get any search results based on 'query' parameter.

        It first looks if there is a recent search with the same query on the database.
        If it is already in the database it returns the related results.
        If it is not in the database it will call 'Google Custom Search JSON API'
        (https://developers.google.com/custom-search/v1/overview) to get the results + store them + create a response
        with new stored results.

        query_params:
            - query: required, search query
            - page: page that should be returned. Default: 1 - Max: 5
    '''
    @action(detail=False, methods=['get'])
    def search(self, request):
        try:
            query = request.query_params['query']
        except MultiValueDictKeyError:
            return Response({'status': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)

        page = 1
        if 'page' in request.query_params:
            page = int(request.query_params['page'])
        start_index = page * 10

        if page > 5:
            return Response({'status': 'max page limit exceded (max: 3)'})

        try:
            search = Search.objects.get(query=query)
        except ObjectDoesNotExist:
            search = Search(query=query)
            search.save()

        results = search.results.filter(searchmeta__page=page)
        if results:
            serializer = SearchResultSerializer(results, many=True)
            return Response(serializer.data)

        results = list()
        new_results = self.get_new_results(start_index, query)
        if new_results:
            for r in new_results:
                try:
                    result = SearchResult.objects.get(pk=r['id'])

                    results.append(result)
                    search.results.add(result, through_defaults={'page': page})
                except ObjectDoesNotExist:
                    search_result_serializer = SearchResultSerializer(data=r)

                    if search_result_serializer.is_valid():
                        result = search_result_serializer.save()
                        results.append(result)
                        search.results.add(result, through_defaults={'page': page})

            serializer = SearchResultSerializer(results, many=True)
            return Response(serializer.data)
        return Response({'status': 'no results found'})

    def get_new_results(self, start_index, query):
        with open('tokens.json', 'r') as f:
            tokens = json.load(f)

        URI = 'https://www.googleapis.com/customsearch/v1'
        KEY = tokens["key"]
        CX = tokens["cx"]

        r = requests.get(
            f'{URI}?key={KEY}&cx={CX}&start={start_index}&num=10&q={query}'
        )

        if r.status_code == 200:
            results = list()
            if int(r.json()['searchInformation']['totalResults']) > 0:
                for sr in r.json()['items']:
                    if 'cacheId' in sr:
                        sr['id'] = sr.pop('cacheId')
                        results.append(sr)
                return results
        return []
