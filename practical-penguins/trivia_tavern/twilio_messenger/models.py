from django.db import models
from trivia_runner.models import Player

class ScoreTracker(models.Model):
    player_phone = models.CharField(max_length=12)
    team_name = models.CharField(max_length=24, default='')
    points = models.IntegerField(default=0)
    session_code = models.CharField(max_length=6)
    answered_this_round = models.BooleanField(default=False)

    def get_score_list(session_code):
        """get_score_list is a class method that returns all players and their score_list
        for the specified session"""
        return [(x.player_phone, x.points) for x in ScoreTracker.objects.filter(session_code=session_code)]

    def get_team_score_list(session_code):
        """As above, but for each team"""
        # First get all possible team names
        team_names = [t.team_name for t in Player.objects.all()]
        team_names = list(dict.fromkeys(team_names))
        team_scores = []
        for team in team_names:
            team_track = ScoreTracker.objects.filter(team_name=team, session_code=session_code)
            team_score = sum([x.points for x in team_track])
            team_scores.append((team, team_score))

        return team_scores


    def winner(session_code, score_list):
        """winner is a class method that returns the winning player
        for the specified session, 'score_list' should be the output
        of one of the above two functions"""
        return max(score_list, key=lambda x:x[1])[0]
