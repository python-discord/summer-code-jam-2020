import pytest
from djangocities.user.models import CustomUser as User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    user = User.objects.get(username="john")
    assert user is not None
