from django.shortcuts import render
from .models import Location
from dal import autocomplete

# Create your views here.
class LocationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        # if not self.request.user.is_authenticated():
        #     return User.objects.none()

        qs = Location.objects.all()

        if self.q:
            qs = qs.filter(location_title__istartswith=self.q)

        return qs