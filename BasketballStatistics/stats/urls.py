from django.urls import path


from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("addAthlete",views.athlete_page, name="add_athlete"),
    path("addGame",views.add_game,name="add_game"),
    path("practices",views.practice_stats,name="practice_stats"),
    path("addAthlete/<int:player_id>/",views.get_player,name="get_player")
]