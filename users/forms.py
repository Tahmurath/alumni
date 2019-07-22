from django import forms
from dal import autocomplete
from django.contrib.auth.forms import UserChangeForm
from .models import User as NewUserModel
from .models import Sabteahval
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


class UserForm(UserChangeForm):
    class Meta:
        widgets = {
            'born_location': autocomplete.ModelSelect2(url='location-autocomplete'),
            'country': autocomplete.ModelSelect2(url='country-autocomplete'),
        }

    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     self.fields['person_born_date'] = JalaliDateField(label=_('Birthday'), widget=AdminJalaliDateWidget)


class NewStdForm(forms.ModelForm):
    class Meta:
        model = NewUserModel
        fields = (
            'first_name', 'last_name', 'person_melli_code', 'person_gender', 'person_shen_number', 'mobile_number')


class NewStdVerifyForm(forms.ModelForm):
    class Meta:
        model = Sabteahval
        fields = (
            'id', 'first_name', 'last_name', 'person_father_name', 'person_shen_number', 'person_born_date',
            'person_melli_code',
            'mobile_number')

    def __init__(self, *args, **kwargs):
        super(NewStdVerifyForm, self).__init__(*args, **kwargs)
        self.fields['person_born_date'] = JalaliDateField(label=_('Birthday'),  # date format is  "yyyy-mm-dd"
                                                          widget=AdminJalaliDateWidget
                                                          # optional, to use default datepicker
                                                          )


class Etelaate_fardi(forms.ModelForm):
    class Meta:
        model = NewUserModel
        fields = (
            'first_name', 'last_name', 'person_melli_code', 'person_shen_number', 'person_born_date',
            'born_location', 'person_father_name', 'person_gender', 'military', 'isargari', 'marital_status',
            'physical_condition', 'number_of_children', 'avatar')

    def __init__(self, *args, **kwargs):
        super(Etelaate_fardi, self).__init__(*args, **kwargs)
        self.fields['person_born_date'] = JalaliDateField(label=_('Birthday'),  # date format is  "yyyy-mm-dd"
                                                          widget=AdminJalaliDateWidget
                                                          # optional, to use default datepicker
                                                          )
