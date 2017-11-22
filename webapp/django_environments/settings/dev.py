from .base import *

INSTALLED_APPS += [
	'django_extensions',
	'debug_toolbar',
] 

MIDDLEWARE += (
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1', )

def show_toolbar(request):
    if request.is_ajax():
        return False
    return True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'django_environments.settings.dev.show_toolbar',
}


