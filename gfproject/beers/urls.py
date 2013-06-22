from django.conf.urls import patterns, url

from beers import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login', views.login),
    url(r'^logout', views.logout),
    url(r'^callback$', view=views.callback, name='callback')
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)