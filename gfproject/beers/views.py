import os
import untappd

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.conf import settings

from beers.models import Brewery, Beer

class IndexView(generic.ListView):
    template_name = 'beers/index.html'
    context_object_name = 'beer_list'

    def get_queryset(self):
        return Beer.objects.order_by('brewery__name')

def detail(request, beer_id):
	beer = get_object_or_404(Beer, pk=beer_id)

	if 'access_token' in request.session:
		client = untappd.Untappd(access_token=request.session['access_token'])
		untappd_beer = client.beer(beer.untappd_id)
	else:
		untappd_beer = None

	return render(request, 'beers/detail.html', { 'beer': beer, 'untappd_beer': untappd_beer })

def login(request):
	client = untappd.Untappd(client_id=os.environ['UNTAPPD_CLIENT_ID'], client_secret=os.environ['UNTAPPD_CLIENT_SECRET'], redirect_url=os.environ['UNTAPPD_REDIRECT_URL'])
	auth_url = client.oauth.auth_url()

	return HttpResponseRedirect(auth_url)

def logout(request):
	request.session.clear()

	return HttpResponseRedirect('/')

def callback(request):
	client = untappd.Untappd(client_id=os.environ['UNTAPPD_CLIENT_ID'], client_secret=os.environ['UNTAPPD_CLIENT_SECRET'], redirect_url=os.environ['UNTAPPD_REDIRECT_URL'])
	code = request.GET.get('code')
	access_token = client.oauth.get_token(code)

	request.session['access_token'] = access_token

	client.set_access_token(access_token)
	user = client.user()
	request.session['user_name'] = user['user']['user_name']

	return HttpResponseRedirect('/')

