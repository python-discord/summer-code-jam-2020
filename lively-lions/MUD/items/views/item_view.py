from django.http import JsonResponse
from django.forms.models import model_to_dict
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
    dict_obj = model_to_dict(item_cat)
    return JsonResponse(dict_obj)


def small_item_view(request, item_id):
    small_item = Small_Item.objects.get(pk=item_id)
    dict_obj = model_to_dict(small_item)
    return JsonResponse(dict_obj)


def large_item_view(request, item_id):
    large_item = Large_Item.objects.get(pk=item_id)
    dict_obj = model_to_dict(large_item)
    return JsonResponse(dict_obj)
