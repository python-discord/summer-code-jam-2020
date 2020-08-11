# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# # # Character - Item : Character get drop Item
# @login_required
# def pickup_item(request, item_id):
#     return HttpResponse(f"Pickup item with id: {item_id}")
# # Character drop Item
# @login_required
# def drop_item(request, item_id):
#     return HttpResponse(f"Drop item with id: {item_id}")
# # inventory
# @login_required
# def get_inventory_items(request):
#     return HttpResponse(f"Get inventory items")
# @login_required
# def add_item_to_inventory(request, item_id):
#     return HttpResponse(f"Add item to inventory with id: {item_id}")
# # character equip item
# @login_required
# def equip_item(request, item_id):
#     return HttpResponse(f"Equip item with id: {item_id}")
# @login_required
# def unequip_item(request, item_id):
#     return HttpResponse(f"Unequip item with id: {item_id}")
