import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from weather.tasks import update_weather_for_user  # noqa: F401


@login_required
def index(request: HttpRequest) -> HttpResponse:

    # TODO Replace this big hardcoded dictionay by the functions
    # that return the needed data from the database

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


@login_required
def update_location(request: HttpRequest) -> HttpResponse:
    """Updates the user models geolocation with location
    from url parameters and redirects to dashboard page."""

    try:
        longitude = float(request.GET.get("longitude"))
        latitude = float(request.GET.get("latitude"))

        # Update user model
        user = request.user

        # Update previous location
        if user.location_set.exists():
            location = user.location_set.last()
            location.longitude = longitude
            location.latitude = latitude

            location.save()

        else:  # Create new location
            user.location_set.create(
                longitude=longitude,
                latitude=latitude,
            )

        # Update weather for new user location
        update_weather_for_user(user)

    except TypeError:
        # There is no need to log any error or display
        # it for the user, so we can skip that.
        pass

    return redirect("index")
