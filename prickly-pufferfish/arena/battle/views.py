from django.views.generic import FormView
from .forms import BattleForm


class BattleView(FormView):
    form_class = BattleForm
