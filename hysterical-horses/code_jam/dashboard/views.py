import requests
import re
from typing import List
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse
import textwrap
import string
from users.mixins import level_check
from .models import Search
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
            duckduckgo_cryptic = {'%20': ' ',
                                  '%20C': ','}
            text_search = re.search(pat, entry['Result'])
            title = text_search.group(1)
            info = text_search.group(2).replace('<br>', "").replace(',', '')
            if '<a>' in title or '</a>' in title:
                url = entry['FirstURL']
                title  = url[::-1][:url[::-1].index('/')][::-1] # need to fix this up: DONE
                for k in duckduckgo_cryptic:
                    title.replace(k, duckduckgo_cryptic[k])
                base_url = 'https://api.duckduckgo.com/'
                payload_crypt_info = {"q": title, "format": "json", "pretty": "1"}
                crypt_info_json = requests.get(base_url, params = payload_crypt_info).json() 
            punc = string.punctuation

            # js-freindly-title makes sure the element does not have a punctuation in the id (')
            return {'title': title,
                    'info': info,
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

# needs to be global otherwise session gets
# reinstantiated each time
global hist_store;
hist_store = SessionStore()
@login_required()
def engine_results(request, search_text: str):
    """ Renders a page for the request  """
    # queries that have some problems:
    # prevent long searches from overflowing
    wrapper = textwrap.TextWrapper(width=15)
    shortened = wrapper.wrap(text=search_text)[0]
    if shortened != search_text:
        shortened += '...'

    # session info for history
    
    try:
        old_val = hist_store['history']
        hist_store['history'] = old_val + [shortened]
    except KeyError:
        hist_store['history'] = [shortened]
    hist = hist_store['history'][-3:]

    
    res = search_query(search_text)

    if search_text not in Search.objects.filter(author=request.user, content=search_text):
        this_search = Search.objects.create(
            author=request.user,
            content=search_text
        )
        this_search.save()

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
        'top_results': top_results,
        'other_results':  other_results,
        'description': desc,
        'version_number': '1.1',
        'entries_length': len(top_results + other_results),
        'past_history': hist, 
    }

    return render(request, 'dashboard/search-engine/results.html', context=context)


@login_required()
@user_passes_test(lambda user: level_check(user, unlock=3), login_url="dashboard-index", redirect_field_name=None)
def chat_room(request, room_name):
    context = {'room_name': room_name}
    return render(request, 'dashboard/chat_room.html', context)





# things to do:
# if not enough info is given for a single entry call the entry as a query and send results (for example: )
# llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch

