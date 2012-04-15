from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
	url(r'^$', 'mapsapp.views.index'),
	url(r'^mapsapp/$', 'mapsapp.views.index'),
	url(r'^mapsapp/map/$', 'mapsapp.views.map'),
	url(r'^mapsapp/geoip/$', 'mapsapp.views.geoip') 
)
