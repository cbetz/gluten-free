from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from beers import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login', views.login),
    url(r'^logout', views.logout),
    url(r'^callback$', view=views.callback, name='callback'),
    url(r'^(?P<beer_id>\d+)/$', views.detail, name='detail'),
    url(r'^info', TemplateView.as_view(template_name='beers/info.html'), name='info'),
)