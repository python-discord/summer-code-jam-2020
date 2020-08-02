import pytest
from djangocities.cities.models import City
from djangocities.user.models import CustomUser as User
from djangocities.sites.models import Site


@pytest.mark.django_db
def test_site():
    city = City(name='testcity', description='my test city', slug='testcity')
    city.save()

    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    user.save()

    address = 0

    site = Site(city=city, user=user, address=address)
    site.save()
    site = Site.objects.get(city=city, address=address)

    assert site is not None
