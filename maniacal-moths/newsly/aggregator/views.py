from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
from .db_gen import Database_Generator
from django.shortcuts import redirect
from users.models import Profile


class ArticleDetailView(DetailView):
    """View for displaying individual article details"""

    model = Article


class ArticleListView(ListView):
    """View for displaying all articles"""

    paginate_by = 5
    model = Article
    template_name = "aggregator/home.html"
    context_object_name = "articles"
    queryset = Article.objects.order_by("-published_date")
    # order by latest articles first


class PoliticsListView(ArticleListView):
    """Categorises Political Articles"""

    queryset = Article.objects.filter(topic="politics").order_by("-published_date")


class TechnologyListView(ArticleListView):
    """Categorises Technology Articles"""

    queryset = Article.objects.filter(topic="tech").order_by("-published_date")


class BusinessListView(ArticleListView):
    """Categorises Business Articles"""

    queryset = Article.objects.filter(topic="business").order_by("-published_date")


class FinanceListView(ArticleListView):
    """Categorises Finance Articles"""

    queryset = Article.objects.filter(topic="finance").order_by("-published_date")


class EconomicsListView(ArticleListView):
    """Categorises Economics Articles"""

    queryset = Article.objects.filter(topic="economics").order_by("-published_date")


class EntertainmentListView(ArticleListView):
    """Categorises Entertainment Articles"""

    queryset = Article.objects.filter(topic="entertainment").order_by("-published_date")


class SportsListView(ArticleListView):
    """Categorises Sports Articles"""

    queryset = Article.objects.filter(topic="sports").order_by("-published_date")


class WorldListView(ArticleListView):
    """Categorises World Articles"""

    queryset = Article.objects.filter(topic="world").order_by("-published_date")


class NewsListView(ArticleListView):
    """Categorises General Articles"""

    queryset = Article.objects.filter(topic="news").order_by("-published_date")


def refresh_database(request):
    """Add latest articles to the database"""
    db_maker = Database_Generator()
    if request.user.is_authenticated:
        # Generate articles based on user's preferences
        db_maker.generate_db(
            lang=Profile.objects.get(user=request.user.id).language,
            country=Profile.objects.get(user=request.user.id).country,
        )
    else:
        # Generate English articles from Australia - default
        db_maker.generate_db()
    return redirect("/")


def about(request):
    return render(request, "aggregator/about.html", {"title": "About"})
