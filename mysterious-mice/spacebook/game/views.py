from django.shortcuts import render
from django.views.generic import View
from .models import HighScore
from .utils import *


class GameView(View):
    # def get_context_data(self, **kwargs):
    #     context = super(GameView, self).get_context_data(**kwargs)
    #     return context
    def get(self, request):
        game_data = get_game(request)
        command = self.request.GET.get("command")
        parse_command(request, game_data, command)

        context = game_data
        return render(request, "game/game.html", context)

    def post(self, request):
        game_data = get_game(request)
        command = self.request.POST.get("command")
        parse_command(request, game_data, command)

        context = game_data
        return render(request, "game/game.html", context)