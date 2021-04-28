from .settings import *

DEBUG = False

ALLOWED_HOSTS=["*"]


STATIC_URL = "/static/"

STATIC_ROOT = "/web/static"

# add new settings for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "mailhog"
EMAIL_PORT = 1025