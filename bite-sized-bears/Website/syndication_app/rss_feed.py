from django.contrib.syndication.views import Feed
from syndication_app.models import Post, User, Community


class LatestEntriesFeed(Feed):
    title = "Community Posts"
    link = "/rss/feed/community"
    description = "A Mix of community posts from all the communities personalised for you"

    def get_object(self, request, username):
        return User.objects.get(name=username)

    def items(self, obj):
        return Post.objects.filter(publisher__in=Community.objects
                                   .prefetch_related('subscribers')
                                   .filter(subscribers__name__exact=obj.name)
                                   .values('id'))

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_author_name(self, item):
        return item.author.name

    def item_author_email(self):
        return 'ww@ww.com'

    def item_author_link(self, item):
        print("http://localhost:8000/" + item.author.get_absolute_url())
        return item.author.get_absolute_url()

    def item_pubdate(self, item):
        return item.creation_date

    def item_categories(self, item):
        print(item.publisher.name)
        return [item.publisher.name]
