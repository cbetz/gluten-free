from django.db import models

class Brewery(models.Model):
    untappd_id = models.IntegerField()
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    logo = models.URLField(max_length=200)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "breweries"

class Beer(models.Model):
    untappd_id = models.IntegerField()
    name = models.CharField(max_length=200)
    brewery = models.ForeignKey(Brewery)
    label = models.URLField(max_length=200)
    gluten_removed = models.BooleanField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __unicode__(self):
    	return self.name