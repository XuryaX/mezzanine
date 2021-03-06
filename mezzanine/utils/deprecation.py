from django.conf import settings


# Middleware mixin for Django 1.10
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    class MiddlewareMixin(object):
        pass


MIDDLEWARE_SETTING = settings.MIDDLEWARE if hasattr(settings, 'MIDDLEWARE') \
                                        and settings.MIDDLEWARE is not None \
                                        else settings.MIDDLEWARE_CLASSES
