from django.shortcuts import render
from django.http import request
# Create your views here.
from django.http import HttpResponse
from .forms import loginForm
# from django.utils.translation import gettext_lazy
from django.utils.translation import ugettext, activate, get_language
from students.models import Center, Field, Term
from users.models import Country, Location
from django.utils.translation import LANGUAGE_SESSION_KEY
from dal import autocomplete
from users.models import User

# activate, ugettext, get_language


"""
    request.session['fghfghf'] = "34534534"

    output = ugettext('Test') + ' ' \
             + request.META['HTTP_ACCEPT_LANGUAGE'] \
             + ' ' + get_language() + " " \
             + request.session['fghfghf'] \
"""


class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        # if not self.request.user.is_authenticated():
        #     return User.objects.none()

        qs = Country.objects.all()

        if self.q:
            qs = qs.filter(country_title__startswith=self.q)

        return qs


class TermAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        # if not self.request.user.is_authenticated():
        #     return User.objects.none()

        qs = Term.objects.all()

        if self.q:
            qs = qs.filter(term_title__istartswith=self.q)

        return qs


class CenterAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        # if not self.request.user.is_authenticated():
        #     return User.objects.none()

        qs = Center.objects.all()

        if self.q:
            qs = qs.filter(center_title__istartswith=self.q)

        return qs


class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        # if not self.request.user.is_authenticated():
        #     return User.objects.none()

        qs = User.objects.all()

        if self.q:
            qs = qs.filter(first_name__istartswith=self.q)

        return qs


class FieldAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        # if not self.request.user.is_authenticated():
        #     return User.objects.none()

        qs = Field.objects.all()

        if self.q:
            qs = qs.filter(field_title__istartswith=self.q)

        return qs


def index(request):
    # activate('fr')

    output = ugettext('English') + ' ' + ugettext('Persian') + ' ' + ugettext('Persian') + ' ' + ugettext('Persian')

    return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the Home index.")


def loginsignup(request):
    context = {
        'num_students': 12,
        'loginForm': loginForm,
    }

    return render(request, 'loginsignup.html', context=context)
