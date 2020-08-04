from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime


# @login_required
def index(request):

    # TODO Replace this big hardcoded dictionay by the functions
    # that return the needed data from the database

    # TODO: Convert the sunrise / sunset time to local time, not UTC.

    context = {
        "weather": {
            "degree_celsius": 39,
            "degree_fahrenheit": 102.2,
            "astral_information": {
                "sunrise": datetime.datetime.utcnow(),
                "sunset": datetime.datetime.utcnow(),
                "moon_phase": 11.5
            }
        },
        "wikipedia_article": {
            "title": "Python (programming language)",
            "content": ("Python is an interpreted, high-level, general-purpose programming language. "
                        "Created by Guido van Rossum and first released in 1991, Python's design "
                        "philosophy emphasizes code readability with its notable use of significant "
                        "whitespace. Its language constructs and object-oriented approach aim to help "
                        "programmers write clear, logical code for small and large-scale projects..."),
            "url": "https://en.wikipedia.org/wiki/Python_(programming_language)"
        },
        "news_articles": [
            {
                "title": "Summer-Code-Jam 2020 just started",
                "content": ("The 7th code jam for the python discord server just started "
                            "a few days ago. Team Concerned Coyotes will win it. No "
                            "questions asked."),
                "url": "#"
            },
            {
                "title": "Coronavirus killed all Flat Earth Believers",
                "content": ("The Coronavirus had a mutation which seems to target flat "
                            "earth believers especially hard. Nearly all of them died."),
                "url": "#"
            }
        ],
        "todos": [
            "Visit Doctor xyz",
            "Buy a nice gift for my dog",
            "Check out Django for the Code Jam"
        ],
    }

    return render(request=request,
                  template_name='dashboard.html',
                  context=context)
