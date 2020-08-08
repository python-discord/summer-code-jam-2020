import pytest
from django.shortcuts import reverse
from core.factories import ListingFactory


@pytest.mark.django_db
def test_get_listing_list_view_is_ok(client):
    response = client.get(reverse("listings"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_listing_search_filters_queryset_results(client):
    listing_1 = ListingFactory(item__product__name="Find Me")
    listing_2 = ListingFactory(item__product__name="Not Found")
    url = f"{reverse('listings')}?search=find"
    response = client.get(url)
    content = str(response.content)
    assert listing_1.item.product.name in content
    assert listing_2.item.product.name not in content
