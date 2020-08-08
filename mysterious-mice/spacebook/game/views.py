from django.shortcuts import render
from django.views.generic import View
from .models import HighScore
from .utils import get_game, parse_command


class GameView(View):
    def get(self, request):
        game_data = get_game(request)
        context = game_data
        return render(request, "game/game.html", context)

    def post(self, request):
        game_data = get_game(request)
        # game_data = new_game()
        command = self.request.POST.get("command")
        if command is not None and command != "":
            game_data = parse_command(request, game_data, command)
        context = game_data
        return render(request, "game/game.html", context)
