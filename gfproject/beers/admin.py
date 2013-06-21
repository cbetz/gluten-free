from django.contrib import admin
from beers.models import Brewery, Beer

admin.site.register(Brewery)
admin.site.register(Beer)