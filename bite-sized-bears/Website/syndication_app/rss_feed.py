from django.contrib.syndication.views import Feed

from .models import Post, User, Community


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
                                   .values('id')).order_by('-creation_date')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_author_name(self, item):
        return item.author.name

    def item_author_link(self, item):
        return item.author.get_absolute_url()

    def item_pubdate(self, item):
        return item.creation_date

    def item_categories(self, item):
        return [item.publisher.name]
