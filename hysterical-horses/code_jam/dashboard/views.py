from django.shortcuts import render
import requests
import json

def index(request):
    return render(request, 'dashboard/index.html')

def search_query(search: str):
    """ Takes in a search query and requests an API for results  """
    base_url = 'https://api.duckduckgo.com/'
    payload = {"q": search, "format": "json", "pretty": "1"}
    results = requests.get(base_url, params = payload).json()
    return results

print(search_query('python'))

