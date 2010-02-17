from hello_newsroom.configs.common.settings import *

# Debugging
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Database
DATABASE_HOST = 'db.tribapps.com'
DATABASE_PORT = '5433'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://media.tribapps.com/hello_newsroom/'

# Predefined domain
MY_SITE_DOMAIN = 'hello_newsroom.tribapps.com'

# Email
EMAIL_HOST = 'mail.tribapps.com'

# Caching
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# S3
AWS_S3_URL = 's3://media.tribapps.com/hello_newsroom/'

# logging
import logging.config
LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(LOG_FILENAME)