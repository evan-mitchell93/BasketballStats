from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

############################
# User Accounts Model/Form #
############################

class SevenOaksUser(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']

############################
## Athlete Model and Form ##
############################
class Athlete(models.Model):
    #Teams available at SOCS
    #teams options broke python anywhere
    #look in to this


    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    team = models.CharField(max_length=8)
    position = models.CharField(max_length=1)
    jersey = models.IntegerField()
    username = models.CharField(max_length=30,null=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    

class AthleteForm(ModelForm):
    class Meta:
        model = Athlete
        exclude = ('username',)


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
    last_opp = models.CharField(max_length=4)

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


