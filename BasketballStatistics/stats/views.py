from django.shortcuts import HttpResponse, render

from .models import *

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

#render a form for adding a new game/update game result to application database.
def add_game(request):
    form = GameForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Thank you for adding a game")
    return render(request,"stats/game_form.html",{"form":form})


def practice_stats(request):
    test = Stats.objects.filter(player__last_name__contains="Easton")
    return HttpResponse(test)