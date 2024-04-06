from django.urls import path


from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("addAthlete",views.athlete_page, name="add_athlete"),
    path("addGame",views.add_game,name="add_game")
]