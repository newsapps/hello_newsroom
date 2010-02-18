from hello_newsroom.configs.common.settings import *

# Debugging
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://your-bucket-name.s3.amazonaws.com/hello_newsroom/'

# Predefined domain
MY_SITE_DOMAIN = 'your-ec2-instance-dns-name.amazonaws.com'

# Email
EMAIL_HOST = 'mail'

# Caching
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# logging
import logging.config
LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(LOG_FILENAME)