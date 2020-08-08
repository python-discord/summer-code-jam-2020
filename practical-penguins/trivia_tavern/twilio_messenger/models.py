from django.db import models
from trivia_runner.models import Player


class ScoreTracker(models.Model):
    player_name = models.CharField(max_length=24)
    points = models.IntegerField(default=0)
    session_code = models.CharField(max_length=6)
    answered_this_round = models.BooleanField(default=False)

    @staticmethod
    def get_score_list(session_code):
        """get_score_list is a class method that returns all players and their score_list
        for the specified session"""
        return [(x.player_name, x.points) for x in ScoreTracker.objects.filter(session_code=session_code)]

    @staticmethod
    def winner(session_code):
        """winner is a class method that returns the winning player
        for the specified session"""
        score_list = ScoreTracker.get_score_list(session_code)
        return max(score_list, key=lambda x: x[1])[0]
