from hello_newsroom.configs.common.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://media-beta.tribapps.com/hello_newsroom/'

# Predefined domain
MY_SITE_DOMAIN = 'ec2-184-73-1-9.compute-1.amazonaws.com'

# Email
EMAIL_HOST = 'localhost'

# Caching
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# GOOGLE_MAPS_API_KEY = 'ABQIAAAA3uGjGrzq3HsSSbZWegPbIhSMhkig1Gd5B_2j4H1Xz7hsATFBFhSnBeYqZ7F7xlyJh-_KEClsWgAO6Q' # all amazonaws.com

# If you want to use Django Debug Toolbar, you need to list your IP address here
INTERNAL_IPS = ('0.0.0.0')

# logging
import logging.config
LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(LOG_FILENAME)