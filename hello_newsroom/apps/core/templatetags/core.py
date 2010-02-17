from django import template
from django.conf import settings
from urlparse import urljoin
from urllib import quote_plus

register = template.Library()
 
@register.simple_tag
def url_prefix():
    """Render a suitable prefix for a fully qualified URL.  Designed to work with
    the Django 'url' tag, so this will not include the trailing slash.  Uses
    settings.MY_SITE_DOMAIN and, if defined, settings.MY_SITE_SCHEMA (defaults to http if not defined)
    and settings.MY_SITE_PORT (e.g. 8000; defaults to empty if not defined)"""
    parts = [getattr(settings,'MY_SITE_SCHEMA','http'), '://', getattr(settings,'MY_SITE_DOMAIN')]
    if getattr(settings,'MY_SITE_PORT',False):
        parts.append(':')
        parts.append(settings.MY_SITE_PORT)
    return ''.join(parts)

@register.simple_tag
def build_media_url(uri):
    """
       Take a bit of url (uri) and put it together with the media url
       urljoin doesn't work like you think it would work. It likes to
       throw bits of the url away unless things are just right.
    """
    uri = "/".join(map(quote_plus,uri.split("/")))
    if getattr(settings,'MEDIA_URL',False):
        if uri.startswith('/'):
            return urljoin(settings.MEDIA_URL,uri[1:])
        else:
            return urljoin(settings.MEDIA_URL,uri)
    else:
        return uri

@register.inclusion_tag("core/_gmap.html")
def gmap(gmap_api_version="2"):
    """Return the fragment of JS necessary to inline the Google Maps API on the page, assuming that the Django settings includes
       a value for GOOGLE_MAPS_API_KEY
       """
    assert settings.GOOGLE_MAPS_API_KEY

    return { "gmap_api_version": gmap_api_version,
             "settings": settings 
    }
