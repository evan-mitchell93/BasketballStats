from django.urls import path


from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("addAthlete",views.athlete_page, name="new_athlete"),
    path("practices/new",views.new_practice,name="new_practice"),
    path("practices/freethrows",views.free_throws,name="free_throws"),
    path("practices/shootingdrills",views.shooting_drills,name="shooting_drills"),
    path("practices",views.practices,name="practices"),
    path("practices/freethrows/save",views.free_throws,name="free_throw_save")
]