import pytest
from djangocities.cities.models import City


@pytest.mark.django_db
def test_city():
    city = City(name="testcity", description="my test city", slug="testcity")
    city.save()
    city = City.objects.get(name="testcity")
    assert city is not None
