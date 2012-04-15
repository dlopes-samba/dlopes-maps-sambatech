from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.conf import settings

import os
import pygeoip

##
# redirect to index.html template
##
def index(request):
	return redirect_to_index(request, {})

##
# get IP address and try to geo-localize it
##
def geoip(request):
	ip = request.POST['ip']

	if ip == '':
		return redirect_to_index(request, {
				'error_message': 'Endereco IP nao pode ser vazio.',
				})
	
	geoIp = pygeoip.GeoIP(
				os.path.join(settings.MEDIA_ROOT, 'GeoLiteCity.dat'), 
				flags=pygeoip.const.MEMORY_CACHE)
	try:	
		record = geoIp.record_by_addr(ip)

	except pygeoip.GeoIPError:
		##
		# invalid address, not xxx.xxx.xxx.xxx
		## 
		return redirect_to_index(request, {
				'error_message': '(' + ip + ') nao e um endereco de IP valido.',
				})


	##
	# found nothing
	##
	if record is None:
		return redirect_to_index('mapsapp/index.html', dictionary={
				'error_message': 'Endereco IP fornecido (' + ip + ') nao pode ser geo-localizado.',
				})

	else:
		return render_to_response('mapsapp/map.html',  {
			'ip': ip,
			'latitude': record['latitude'],
			'record': record,
			'longitude': record['longitude'],
			}, context_instance=RequestContext(request))

##
# common function used to redirect to index.html, showing an error message or not
##
def redirect_to_index(request, dictionary):
	return render_to_response('mapsapp/index.html', dictionary, context_instance=RequestContext(request))

