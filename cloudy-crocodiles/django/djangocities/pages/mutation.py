import logging

from djangocities.iam.jwt import load_user
from djangocities.pages.models import Page
from djangocities.sites.models import Site


def resolve_create_page(_, info, data):
    # request = info.context["request"]
    # user = load_user(info)
    # if not user.is_authenticated:
    #     raise Exception("You can't do that!")

    pass


def resolve_update_page(_, info, data):
    pass
