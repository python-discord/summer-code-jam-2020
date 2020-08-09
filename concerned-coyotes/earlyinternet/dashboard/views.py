from django.contrib.auth.decorators import login_required
from django.apps import apps
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from weather.tasks import update_weather_for_user  # noqa: F401

Weather = apps.get_model("weather", "Weather")
WikipediaArticle = apps.get_model("wikipedia", "WikipediaArticle")
Article = apps.get_model("news", "Article")
TodoEntry = apps.get_model("todo", "TodoEntry")


@login_required
def index(request: HttpRequest) -> HttpResponse:
    user = request.user

    context = {}

    # If weather does not exist for the user, it is returned as None
    # and an error / request to set location is shown on the frontend
    if user.location_set.exists():
        user_location = user.location_set.last()
        user_weather = Weather.objects.get_weather_at(user_location.latitude,
                                                      user_location.longitude)

        context.update({
            "weather": {
                "degree_celsius": user_weather.celsius,
                "degree_fahrenheit": user_weather.fahrenheit,
                "astral_information": {
                    "sunrise": str(user_weather.sunrise),
                    "sunset": str(user_weather.sunset)
                },
                "city": user_weather.city,
            }
        })

    else:
        context["weather"] = None

    # Wikipedia article
    wikipedia_article = WikipediaArticle.objects.order_by("-date")[0]
    if wikipedia_article:
        context.update({
            "wikipedia_article": {
                "title": wikipedia_article.title,
                "content": wikipedia_article.content,
                "url": wikipedia_article.url
            }
        })
    else:
        context["wikipedia_article"] = None

    # News articles
    news_articles = Article.objects.order_by("-published_at")[:3]
    context["news_articles"] = []
    for article in news_articles:
        context["news_articles"].append({
            "title": article.title,
            "source": article.source,
            "author": article.author,
            "description": article.description,
            "content": article.content,
            "url": article.url
        })

    # Todos
    todos = TodoEntry.objects.filter(user=user).all()
    context["todos"] = [todo.name for todo in todos]

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
