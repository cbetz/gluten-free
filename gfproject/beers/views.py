import untappd

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from beers.models import Brewery, Beer

client = untappd.Untappd(client_id='', client_secret='', redirect_url='')
auth_url = client.oauth.auth_url()

class IndexView(generic.ListView):
    template_name = 'beers/index.html'
    context_object_name = 'beer_list'

    def get_queryset(self):
        return Beer.objects.order_by('brewery__name')

class DetailView(generic.DetailView):
    model = Beer
    template_name = 'beers/detail.html'

def login(request):
	return HttpResponseRedirect(auth_url)

def logout(request):
	request.session.clear()
	return HttpResponseRedirect('/')

def callback(request):
	code = request.GET.get('code')
	access_token = client.oauth.get_token(code)

	request.session['access_token'] = access_token

	client.set_access_token(access_token)
	user = client.user()
	request.session['user_name'] = user['user']['user_name']

	return HttpResponseRedirect('/')

