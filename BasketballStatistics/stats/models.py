from django.db import models
from django.forms import ModelForm

############################
## Athlete Model and Form ##
############################
class Athlete(models.Model):
    #Teams available at SOCS
    TEAMS = {
        "ElemG" : "Girl's 5th and 6th",
        "MidG" : "Girl's 7th and 8th",
        "VarsityG" : "Girl's Varsity",
        "ElemB" : "Boy's 5th and 6th",
        "MidB" : "Boy's 7th and 8th",
        "VarsityB" : "Boy's Varsity"
    }
    #Basic basketball Positions
    POSITIONS = {
        "1" : "Point Guard",
        "2" : "Shooting Guard",
        "3" : "Small Forward",
        "4" : "Power Forward",
        "5" : "Center"
    }

    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    team = models.CharField(max_length=8,choices=TEAMS)
    position = models.CharField(max_length=1,choices=POSITIONS)
    jersey = models.IntegerField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    

class AthleteForm(ModelForm):
    class Meta:
        model = Athlete
        fields = ["first_name","last_name","team","position","jersey"]


############################
### Game Model and Form  ###
############################
        
class Game(models.Model):
    TEAMS = {
        "ElemG" : "Girl's 5th and 6th",
        "MidG" : "Girl's 7th and 8th",
        "VarsityG" : "Girl's Varsity",
        "ElemB" : "Boy's 5th and 6th",
        "MidB" : "Boy's 7th and 8th",
        "VarsityB" : "Boy's Varsity"
    }

    RESULTS = {
        "W" : "Win",
        "L" : "Loss"
    }
        
    team = models.CharField(max_length=8,choices=TEAMS)
    opponent = models.CharField(max_length=75)
    team_score = models.IntegerField()
    opp_score = models.IntegerField()
    outcome = models.CharField(max_length=1,choices=RESULTS)
    date = models.DateField()

    def __str__(self):
        return f"{self.team} vs {self.opponent} : {self.date}"

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ["team","opponent","team_score","opp_score","outcome","date"]



##########################
# STATS MODELS AND FORMS #
##########################

class Stats(models.Model):
    season = models.CharField(max_length=5)
    player = models.ForeignKey(Athlete,on_delete=models.CASCADE)
    s_type = models.CharField(max_length=9)
    two_taken = models.IntegerField(default=0)
    two_made = models.IntegerField(default=0)
    three_taken = models.IntegerField(default=0)
    three_made = models.IntegerField(default=0)
    ft_taken = models.IntegerField(default=0)
    ft_made = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    turnovers = models.IntegerField(default=0)
    off_rebounds = models.IntegerField(default=0)
    def_rebounds = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.last_name}, {self.s_type}: {self.season}"