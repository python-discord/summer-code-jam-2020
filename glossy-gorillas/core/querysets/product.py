from django.db.models import QuerySet, Count, Max


class ProductQuerySet(QuerySet):
    def most_common(self):
        annot = self.annotate(num=Count("inventoryrecord"))
        highest = annot.aggregate(Max("num"))["num__max"]
        return annot.filter(num=highest)
