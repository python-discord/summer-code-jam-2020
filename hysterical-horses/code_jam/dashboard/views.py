from django.shortcuts import render
import requests
import re
from typing import List


def index(request):
    return render(request, 'dashboard/index.html')

def search_query(search: str, format_text: bool =True):
    """ Takes in a search query and requests an API for results  """
    base_url = 'https://api.duckduckgo.com/'
    payload = {"q": search, "format": "json", "pretty": "1"}
    results = requests.get(base_url, params = payload).json()
    
    if format_text: # formats response
        # NOTE:
        # returns as a list of entries
        # each entry is a dict with keys:
        # title (title of entry)
        # info (information about the entry/ brief description)
        # img_url (a source URL for an image relate to the entry)
        # further_info (a duckduckgo URL for more info about the entry)
        # tags (tags that relate to the entry i.e (#1, places, drinks, animals))
        def format_entry(entry: dict, tags: List):
            """ Formats a single entry  """
            pat = r'>(.*)</a>(.*)'
            text_search = re.search(pat, entry['Result'])
            return {'title': text_search.group(1),
                    'info': text_search.group(2),
                    'img_url': entry['Icon']['URL'],
                    'further_info': entry['FirstURL'],
                    'tags': tags}

        formatted = []
        topics = results['RelatedTopics']
        if results['AbstractText'] != '':
            formatted.append({'description': results['AbstractText']})
        # parsing
        for idx, t in enumerate(topics):
            if 'Name' not in t.keys():
                tags = [f'#{idx + 1}'] # the top results
                formatted.append(format_entry(t, tags))
            else:
                tags = [t['Name'].lower()]
                for nt in t['Topics']:
                    formatted.append(format_entry(nt, tags))
        return formatted

    else:
        return results # else return results as is

def engine_results(request):
    """ Renders a page for the request  """

    search_text = '' # search query

    res = search_query(search_text)
    top_results = []
    other_results = []
    desc = ''
    for r in res:
        if 'tags' in r.keys():
            if r['tags'][0] in ['#1', '#2', '#3']:
                top_results.append(r)
            elif r['tags'][0] not in ['#1', '#2', '#3']:
                other_results.append(r)
        elif 'description' in r.keys():
            desc = r['description']
        
    context = {
        'search': search_text,
        'top_results': top_results,
        'other_results':  other_results,
        'description': desc,
    }
    return render(request, 'dashboard/search-engine/results.html', context=context)

