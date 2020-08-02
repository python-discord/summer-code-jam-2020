import pytest
from djangocities.cities.models import City
from djangocities.user.models import CustomUser as User
from djangocities.sites.models import Site, Page


@pytest.mark.django_db
def test_page():
    city = City(name='testcity', description='my test city', slug='testcity')
    city.save()

    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    user.save()

    address = 0

    site = Site(city=city, user=user, address=address)
    site.save()
    site = Site.objects.get(city=city, address=address)

    filename = "index"

    page = Page(site=site, filename=filename, version='H1', content='Welcome to my site')
    page.save()
    page = Page.objects.get(site=site, filename=filename)

    assert page is not None
