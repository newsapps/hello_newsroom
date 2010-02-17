from hello_newsroom.configs.common.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5433'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://media-beta.tribapps.com/hello_newsroom/'

# Predefined domain
MY_SITE_DOMAIN = 'ec2-204-236-246-222.compute-1.amazonaws.com'

# Email
EMAIL_HOST = 'localhost'

# Caching
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# S3
AWS_S3_URL = 's3://media-beta.tribapps.com/hello_newsroom/'

# GOOGLE_MAPS_API_KEY = 'ABQIAAAA3uGjGrzq3HsSSbZWegPbIhSMhkig1Gd5B_2j4H1Xz7hsATFBFhSnBeYqZ7F7xlyJh-_KEClsWgAO6Q' # all amazonaws.com

# Trib IPs for security
INTERNAL_IPS = ('163.192.12.84','163.192.12.108','163.192.12.32')

# logging
import logging.config
LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(LOG_FILENAME)