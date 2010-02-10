import logging

from django.shortcuts import render_to_response
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

from geopy import geocoders

from core import models

log = logging.getLogger("hello_world")

# NOTE: Under load, this strategy is likely to max out your Google API Key. 
# Where possible, geocode addresses using client side calls.
GEOCODER = geocoders.Google()
def index(request):
    template_dict = {}
    try:
        query = request.REQUEST['query']
        template_dict['query'] = query
        address, remainder, point = geocode(query)
        template_dict['address'] = address
        template_dict['remainder'] = remainder
        template_dict['point'] = point

        try:
            template_dict['community_area'] = models.CommunityArea.objects.get(geom__contains=point)
        except models.CommunityArea.DoesNotExist:
            pass

        template_dict['stations'] = nearby_stations(point)
    except KeyError:
        pass # no query
    return render_to_response('core/index.html', template_dict)

def geocode(query):
    results = list(GEOCODER.geocode(query,exactly_one=False))
    address = point = remainder = None
    if results:
        first = results[0]
        remainder = results[1:]
        address, lat_lon = first
        point = Point((lat_lon[1], lat_lon[0]))
    
    return (address, remainder, point)

def nearby_stations(point):
    try:
        stations = models.Station.objects.filter(geom__distance_lte=(point,Distance(mi=1)))
        stations = stations.distance(point).order_by('distance')
        return stations
    except Exception, e:
        log.warn("Error finding stations near %s: %s" % (point.wkt, e))
        return None    