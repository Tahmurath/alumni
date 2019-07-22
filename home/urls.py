from django.urls import path
from . import views, anooz
from django.conf.urls import url
from .views import CenterAutocomplete, UserAutocomplete, FieldAutocomplete, TermAutocomplete, CountryAutocomplete



urlpatterns = [

    path('', views.index, name='index'),
    path('loginsignup', views.loginsignup, name='loginsignup'),
    url(r'^user-autocomplete/$', UserAutocomplete.as_view(), name='user-autocomplete'),
    url(r'^center-autocomplete/$', CenterAutocomplete.as_view(), name='center-autocomplete'),
    url(r'^field-autocomplete/$', FieldAutocomplete.as_view(), name='field-autocomplete'),
    url(r'^term-autocomplete/$', TermAutocomplete.as_view(), name='term-autocomplete'),
    url(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete'),
]
