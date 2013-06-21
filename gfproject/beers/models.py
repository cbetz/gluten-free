from django.db import models

class Brewery(models.Model):
    untappd_id = models.IntegerField()
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    country = models.CharField(max_length=100)
    logo = models.URLField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "breweries"

class Beer(models.Model):
    untappd_id = models.IntegerField()
    name = models.CharField(max_length=200)
    brewery = models.ForeignKey(Brewery)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    label = models.URLField(max_length=200)
    
    def __unicode__(self):
    	return self.name