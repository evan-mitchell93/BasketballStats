from django.shortcuts import HttpResponse, render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import *

import datetime

# Create your views here.
def index(request):
    return render(request,"stats/index.html")

#Register new user
def register(request):
    if request.method == "POST":
        form = SevenOaksUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account was created")
            return redirect('index')
        else:
            messages.error(request, "Error creating account")
    else:
        form = SevenOaksUser()
    return render(request, "registration/register.html", {'form' : form})

#render a form for adding a new athlete to the application database.
@permission_required("stats.view_athletes")
def athlete_page(request):
    form = AthleteForm(request.POST)
    if form.is_valid():
        form.save()
        form = AthleteForm()
    #show all athletes will update to be per team
    athletes = Athlete.objects.all()
    return render(request, "stats/athletes.html",{"form" :form,"athletes" :athletes})


def practices(request):
    # Future updates
    return render(request,"stats/practice.html")

def new_practice(request):
    return HttpResponse("TODO")

def free_throws(request):
    if User.objects.filter(username=request.user.username, groups__name='Players').exists():
        u = User.objects.get(username=request.user.username)
        athletes = Athlete.objects.filter(first_name=u.first_name, last_name=u.last_name)
        print("Player")
    elif User.objects.filter(username=request.user.username,groups__name='Admin').exists():
        athletes = Athlete.objects.all()
        print("Not player")
    ft_list = []
    if request.method == 'GET':
        try:
            records = FreeThrows.objects.filter(date=datetime.datetime.today())
        except ObjectDoesNotExist:
            records = []
        finally:
            if len(records) == 0:
                #create record for each athlete
                for ath in athletes:
                    ft = FreeThrows(player=ath,date=datetime.datetime.today(),attempts=0,makes=0)
                    FreeThrows.save(ft)
                    ft_list.append({"player":ft.player,"attempts":ft.attempts,"makes":ft.makes})
            else:
                #records have been created for the team already so get those 
                for record in records:
                    if record.player in athletes:
                        ft_list.append({"player":record.player,"attempts":record.attempts,"makes":record.makes})


    elif request.method == 'POST':
        ##Loop through athlete free throw objects
        ##update the data from there with the new info for makes/attempts
        for ath in athletes:
            ft = FreeThrows.objects.get(player=ath,date=datetime.datetime.today())
            ft.makes = int(request.POST[ath.__str__()+'makes'])
            ft.attempts = int(request.POST[ath.__str__()+'attempts'])
            ft.save()
            ft_list.append({"player":ft.player,"attempts":ft.attempts,"makes":ft.makes})


    return render(request,"stats/free_throw_form.html",{"ft":ft_list})
    

def shooting_drills(request):
    return HttpResponse("TODO")