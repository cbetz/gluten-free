from django.db import models

class Spot(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=5)
    lat = models.DecimalField('Latitude', max_digits=16, decimal_places=14)
    lng = models.DecimalField('Longitude', max_digits=16, decimal_places=14)
    has_food = models.NullBooleanField('GF food?')
    has_beer = models.NullBooleanField('GF beer?')
    has_menu = models.NullBooleanField('GF menu?')
    menu = models.URLField('Menu link')

    def __unicode__(self):
    	return self.name
