from django.contrib import admin

from .models import Farm
from .models import Farmer

admin.site.register(Farm)
admin.site.register(Farmer)
