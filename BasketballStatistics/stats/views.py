from django.shortcuts import HttpResponse, render

from .models import *

import datetime

# Create your views here.
def index(request):
    return render(request,"stats/index.html")

#render a form for adding a new athlete to the application database.
def athlete_page(request):
    form = AthleteForm(request.POST)
    if form.is_valid():
        form.save()
        form = AthleteForm()
    #show all athletes will update to be per team
    athletes = Athlete.objects.all()
    return render(request, "stats/athletes.html",{"form" :form,"athletes" :athletes})


def practices(request):
    athletes = Athlete.objects.filter(team="VarsityG")
    player_list = []
    for ath in athletes:
        test = Stats.objects.all()
        player_list.append(test)
    print(player_list)
    return render(request,"stats/practice.html",{"data":player_list})

def new_practice(request):
    return HttpResponse("TODO")

def free_throws(request):
    #TODO
    #Create for all athletes then return to make form.
    athletes = Athlete.objects.all()
    ft_list = []
    for ath in athletes:
        ft = FreeThrows(player=ath,date=datetime.datetime.today(),attempts=0,makes=0)
        FreeThrows.save(ft)
        ft_list.append({"player":ft.player,"attempts":ft.attempts,"makes":ft.makes})
    return render(request,"stats/free_throw_form.html",{"ft":ft_list})
    

def shooting_drills(request):
    return HttpResponse("TODO")