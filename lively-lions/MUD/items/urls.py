from django.urls import path
from items.views.item_view import (
                                item_category_detail_view,
                                Item_CategoryDetailView,
                                item_category_view,
                                small_item_view,
                                large_item_view,
                                )

urlpatterns = [
    # will be changed later this was for flake8
    # path('items/', include('items.urls')),
    path(
            'items/category/test/<int:pk>/',
            Item_CategoryDetailView.as_view(),
            name='items-test'
            ),
    path('item_view/item_detail/test/', item_category_detail_view),
    path('category/<int:item_id>/', item_category_view),
    path('small_item/<int:item_id>/', small_item_view),
    path('large_item/<int:item_id>/', large_item_view),
]
