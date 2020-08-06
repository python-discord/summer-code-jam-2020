from .market import *  # noqa
from .review import *  # noqa
from .trader import *  # noqa
from .home import *  # noqa
from .inventoryrecord import *  # noqa
from .register import *  # noqa

from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "core/pages/home.html"
