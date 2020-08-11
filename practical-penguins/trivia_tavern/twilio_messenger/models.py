from typing import Tuple, List, Optional

from django.db import models
from trivia_runner.models import Player


class ScoreTracker(models.Model):
    player_phone = models.CharField(max_length=12)
    team_name = models.CharField(max_length=24, default='')
    points = models.IntegerField(default=0)
    session_code = models.CharField(max_length=6)
    answered_this_round = models.BooleanField(default=False)

    @staticmethod
    def get_score_list(session_code: int) -> List[Optional[Tuple[str, int]]]:
        """get_score_list is a class method that returns all players and their score_list
        for the specified session"""
        return [(x.player_phone, x.points) for x in ScoreTracker.objects.filter(session_code=session_code)]

    @staticmethod
    def get_team_score_list(session_code: int) -> List[Optional[Tuple[int, str, int]]]:
        """As above, but for each team"""
        # First get all possible team names
        team_names = [t.team_name for t in Player.objects.all()]
        team_names = list(dict.fromkeys(team_names))
        team_scores = []
        for i, team in enumerate(team_names, start=1):
            team_track = ScoreTracker.objects.filter(team_name=team, session_code=session_code)
            team_score = sum([x.points for x in team_track])
            team_scores.append((i, team, team_score))

        return team_scores

    @staticmethod
    def winner(score_list: List[Optional[Tuple[int, str, int]]]) -> Optional[str]:
        """winner is a class method that returns the winning player
        for the specified session, 'score_list' should be the output
        of one of the above two functions"""
        sorted_score_list = sorted(score_list, key=lambda x: x[2], reverse=True)
        if len(sorted_score_list) > 0:
            return sorted_score_list[0][1]
        else:
            return None
