import requests
import re
from typing import List
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import textwrap
import string
# import clipboard # for some debugging


@login_required()
def index(request):
    return render(request, 'dashboard/index.html')


def search_query(search: str, format_text: bool =True):
    """ Takes in a search query and requests an API for results  """
    base_url = 'https://api.duckduckgo.com/'
    payload = {"q": search, "format": "json", "pretty": "1"}
    results = requests.get(base_url, params = payload).json()
    # clipboard.copy(str(results)) # REMEMBER TO COMMENT IN AFTER DEBUGGING
    
    if format_text:  # formats response
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
            title = text_search.group(1)
            punc = string.punctuation

            # js-freindly-title makes sure the element does not have a punctuation in the id (')
            return {'title': text_search,
                    'info': text_search.group(2).replace('<br>', "").replace(',', ''),
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


@login_required()
def engine_results(request):
    """ Renders a page for the request  """
    search_text = 'Thalassery' # search query
    # queries that have some problems:
    # "Thalissery"
   

    # prevent long searches from overflowing
    wrapper = textwrap.TextWrapper(width=43)
    shortened = wrapper.wrap(text=search_text)[0]
    if shortened != search_text:
        shortened += '...'

    
    res = search_query(search_text)
    top_results = []
    other_results = []
    desc = ''
    for r in res:
        if 'tags' in r.keys():
            if r['tags'][0] in ['#1', '#2', '#3']:
                top_results.append(r)
            else:
                other_results.append(r)
        elif 'description' in r.keys():
            desc = r['description']
        
    context = {
        'search': search_text,
        'shortened': shortened,
        'top_results': top_results,
        'other_results':  other_results,
        'description': desc,
    }
    return render(request, 'dashboard/search-engine/results.html', context=context)


@login_required()
def chat_room(request, room_name):
    context = {'room_name': room_name}
    return render(request, 'dashboard/chat_room.html', context)


# fixes:
# 


# things to do:
# if not enough info is given for a single entry call the entry as a query and send results
