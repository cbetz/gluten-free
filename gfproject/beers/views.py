from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from beers.models import Brewery, Beer

class IndexView(generic.ListView):
    template_name = 'beers/index.html'
    context_object_name = 'beer_list'

    def get_queryset(self):
        return Beer.objects.order_by('brewery__name')
