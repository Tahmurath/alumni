from django import forms
from django.forms.models import ModelForm
from .models import Student, Center
from dal import autocomplete
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class StudentForm(forms.ModelForm):
    # center_id = forms.ModelChoiceField(
    #     queryset=Center.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='center-autocomplete')
    # )

    # raw_id_fields = ["person_id"]
    # center_id = forms.ModelChoiceField(
    #     queryset=Center.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='center-autocomplete')
    # )
    class Meta:
        model = Student
        # autocomplete_fields = "center_id"
        fields = ('person', 'center', 'field', 'std_code', 'term',
                  'military', 'start_date', 'stop_date')
        # fields = '__all__'
        widgets = {
            'person': autocomplete.ModelSelect2(url='user-autocomplete'),
            'center': autocomplete.ModelSelect2(url='center-autocomplete'),
            'field': autocomplete.ModelSelect2(url='field-autocomplete'),
            # 'term': autocomplete.ModelSelect2(url='term-autocomplete'),
        }
