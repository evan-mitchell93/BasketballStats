from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Athlete)
admin.site.register(Game)