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


##########################
# STATS MODELS AND FORMS #
##########################

class Stats(models.Model):
    player = models.ForeignKey(Athlete,on_delete=models.CASCADE)
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
        return f"{self.player.last_name}"
    
class FreeThrows(models.Model):
    player = models.ForeignKey(Athlete,on_delete=models.CASCADE)
    date = models.DateField()
    attempts = models.IntegerField(default=0)
    makes = models.IntegerField(default=0)

    @property
    def percentage(self):
        if self.attempts != 0:
            return (self.makes / self.attempts) * 100
        else:
            return 0

    def __str__(self):
        return f"{self.player.last_name} : FT Percentage - {self.percentage:.2f}% : Practice - {self.date}"

class ShootingDrill(models.Model):
    player = models.ForeignKey(Athlete,on_delete=models.CASCADE)
    drill_name = models.CharField(max_length=20)
    two_taken = models.IntegerField()
    two_made = models.IntegerField()
    three_taken = models.IntegerField()
    three_made = models.IntegerField()

    @property
    def two_percentage(self):
        if self.two_taken != 0:
            return (self.two_made / self.two_taken) * 100
        else:
            return 0
    @property
    def three_percentage(self):
        if self.three_taken !=0:
            return (self.three_made / self.three_taken) * 100
        else:
            return 0
    def __str__(self):
        return f"{self.player.last_name}: Drill: {self.drill_name} \n 2p% {self.two_percentage:.2f} \
        3p% {self.three_percentage:.2f}"

#Will use for managing dates for drills    
class Practice(models.Model):
    date = models.DateField()


