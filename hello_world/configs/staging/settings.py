from hello_world.configs.common.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Database
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5433'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://media-beta.tribapps.com/hello_world/'

# Predefined domain
MY_SITE_DOMAIN = 'ec2-75-101-207-40.compute-1.amazonaws.com'

# Email
EMAIL_HOST = 'localhost'

# Caching
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# S3
AWS_S3_URL = 's3://media-beta.tribapps.com/hello_world/'

# Trib IPs for security
INTERNAL_IPS = ('163.192.12.84','163.192.12.108','163.192.12.32')

# logging
import logging.config
LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(LOG_FILENAME)