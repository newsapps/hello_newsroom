from django.contrib.gis.db import models

# This is an auto-generated Django model module created by ogrinspect.
# ./manage ogrinspect data/maps/community_areas/Community_area.shp CommunityArea --name-field=community --srid=4269 --mapping 
# followed by a little trimming/editing

# http://egov.cityofchicago.org/webportal/COCWebPortal/COC_ATTACH/community_area.zip

class CommunityArea(models.Model):
    area_number = models.CharField(max_length=2)
    community = models.CharField(max_length=80)
    geom = models.PolygonField(srid=4269)
    objects = models.GeoManager()

    def __unicode__(self): return self.community

# Auto-generated `LayerMapping` dictionary for CommunityArea model
communityarea_mapping = {
    'area_number' : 'AREA_NUMBE',
    'community' : 'COMMUNITY',
    'geom' : 'POLYGON',
}


class Station(models.Model):
    shortname = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    lines = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    ada = models.IntegerField()
    legend = models.CharField(max_length=5)
    alt_legend = models.CharField(max_length=5)
    weblink = models.CharField(max_length=250)
    geom = models.PointField(srid=4269)
    objects = models.GeoManager()

    def __unicode__(self): return self.name


# Auto-generated `LayerMapping` dictionary for Station model
# ./manage ogrinspect data/maps/cta_stations/DATA_ADMIN_CTASTATION.shp Station --name-field=name --srid=4269 --mapping
# followed by a little trimming/editing

# http://egov.cityofchicago.org/webportal/COCWebPortal/COC_EDITORIAL/CTA_Stations.zip
station_mapping = {
    'shortname' : 'SHORTNAME',
    'name' : 'LONGNAME',
    'lines' : 'LINES',
    'address' : 'ADDRESS',
    'ada' : 'ADA',
    'legend' : 'LEGEND',
    'alt_legend' : 'ALT_LEGEND',
    'weblink' : 'WEBLINK',
    'geom' : 'POINT',
}
