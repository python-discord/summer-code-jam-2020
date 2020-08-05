import pytest
from djangocities.cities.models import City
from djangocities.user.models import CustomUser as User
from djangocities.sites.models import Site
from djangocities.pages.models import Page
from djangocities.folders.models import Folder


@pytest.mark.django_db
def test_page():
    city = City(name='Test', description='my test city', slug='test')
    city.save()

    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    user.save()

    address = 0

    site = Site(city=city, user=user, address=address)
    site.save()
    site = Site.objects.get(city=city, address=address)

    folder = Folder(site=site, owner=user, directory='')
    folder.save()
    folder = Folder.objects.get(site=site, owner=user, directory='')

    filename = "index.html"

    page = Page(owner=user, site=site, folder=folder, filename=filename, version='H1', content='Welcome to my site')
    page.save()
    page = Page.objects.get(site=site, folder=folder, filename=filename)

    assert page is not None
