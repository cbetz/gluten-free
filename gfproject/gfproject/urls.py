from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gfproject.views.home', name='home'),
    # url(r'^gfproject/', include('gfproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^', include('beers.urls')),
    url(r'^beers/', include('beers.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
