from settings_common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.mysql',
        'NAME'      : '',
        'USER'      : '',
        'PASSWORD'  : '',
        'HOST'      : '127.0.0.1',
        'PORT'      : '',
    }
}