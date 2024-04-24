from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Athlete)
admin.site.register(Stats)
admin.site.register(FreeThrows)
admin.site.register(ShootingDrill)