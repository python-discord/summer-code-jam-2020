from django.shortcuts import render
from django.views.generic import View
from .models import HighScore
from .utils import get_game, parse_command


class GameView(View):
    def get(self, request):
        game_data = get_game(request)
        context = game_data
        context.update({"scores": self.get_scores()})
        return render(request, "game/game.html", context)

    def post(self, request):

        game_data = get_game(request)

        command = self.request.POST.get("command")
        if command is not None and command != "":
            game_data = parse_command(request, game_data, command)
        context = game_data
        context.update({"scores": self.get_scores()})
        return render(request, "game/game.html", context)

    def get_scores(self):
        """
        Gets the scores from the database.
        """
        scores = HighScore.objects.order_by("-score")
        score_list = []
        i = len(scores)
        if i > 10:
            i = 10
        while i > 0:
            s = scores[i - 1]
            score_list.insert(0, [s.initials, s.score])
            i -= 1
        return score_list
