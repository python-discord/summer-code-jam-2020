from django.http import HttpResponse
from django.shortcuts import render
from items.models import Item_Category, Small_Item, Large_Item
from django.views.generic import DetailView


class Item_CategoryDetailView(DetailView):
    model = Item_Category
    # <app>/<model>_<viewtype>.html


def item_category_detail_view(request):
    item_category = Item_Category.objects.get(pk=1)
    detail = {
            'item_category': item_category
            }
    return render(request, "items/detail.html", detail)


def item_category_view(request, item_id):
    item_cat = Item_Category.objects.get(pk=item_id)
    return HttpResponse(f"Category -> {item_cat.item_title}: {item_cat.type}")


def small_item_view(request, item_id):
    small_item = Small_Item.objects.get(pk=item_id)
    return HttpResponse(f"Item {small_item.item_title}:{small_item.type}")


def large_item_view(request, item_id):
    item_cat = Large_Item.objects.get(pk=item_id)
    return HttpResponse(f"Item {item_cat.item_title}:{item_cat.type}")
