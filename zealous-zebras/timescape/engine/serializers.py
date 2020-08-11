from rest_framework import serializers
from .models import Search, SearchResult


class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchResult
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'
        extra_kwargs = {'results': {'required': False}}
