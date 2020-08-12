from django.db.models import QuerySet


class ListingQuerySet(QuerySet):
    def newest_10(self):
        return self.order_by("-date_listed")[:10]


class TradeQuerySet(QuerySet):
    def newest_10(self):
        return self.order_by("-date_traded")[:10]
