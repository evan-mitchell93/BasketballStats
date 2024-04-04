from django.shortcuts import HttpResponse, render

from .models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to our Statistics App")

#render a form for adding a new athlete to the application database.
def add_athlete(request):
    form = AthleteForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Thank you for adding athlete")
    return render(request, "stats/athlete_form.html",{"form" :form})

#render a form for adding a new game/update game result to application database.
def add_game(request):
    form = GameForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Thank you for adding a game")
    return render(request,"stats/game_form.html",{"form":form})