from django.http import HttpResponse
from django.utils.translation import ugettext, activate
from django.utils.translation import LANGUAGE_SESSION_KEY


class ForceDefaultLanguageMiddleware(object):
    """
    Ignore Accept-Language HTTP headers

    This will force the I18N machinery to always choose settings.LANGUAGE_CODE
    as the default initial language, unless another one is set via sessions or cookies

    Should be installed *before* any middleware that checks request.META['HTTP_ACCEPT_LANGUAGE'],
    namely django.middleware.locale.LocaleMiddleware
    """

    def __init__(self, get_response):



        self.get_response = get_response

    def __call__(self, request):

        if request.session.get('switched') is None:
            request.session[LANGUAGE_SESSION_KEY] = 'fa'
            request.session['switched'] = 'no'

        return self.get_response(request)
"""
    def process_request(self, request):

        request.session[LANGUAGE_SESSION_KEY] = 'fa'

        if request.META.has_key('HTTP_ACCEPT_LANGUAGE'):
            request.session['django_language'] = 'fa'
            # del request.META['HTTP_ACCEPT_LANGUAGE']
"""