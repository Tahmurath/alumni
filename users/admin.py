from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Location, Country
from users.forms import UserForm


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info',
         {'fields': ('first_name', 'last_name', 'email', 'person_melli_code', 'person_shen_number', 'person_gender',
                     'person_father_name',
                     'born_location', 'person_born_date', 'nation', 'country', 'city', 'mobile_number', 'phone_number',
                     'postal_code', 'person_address', 'sajad_person_id', 'isargari', 'marital_status',
                     'physical_condition', 'number_of_children', 'avatar')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username', 'email', 'password1', 'password2', 'person_melli_code', 'person_shen_number', 'person_gender',
            'person_father_name',
            'born_location', 'person_born_date', 'nation', 'country', 'city', 'mobile_number',
            'phone_number', 'postal_code', 'person_address', 'sajad_person_id', 'isargari', 'marital_status',
            'physical_condition', 'number_of_children', 'avatar')}
         ),
    )

    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    form = UserForm
    # raw_id_fields = ["born_location"]
    # widgets = {
    #     'born_location': autocomplete.ModelSelect2(url='location-autocomplete'),
    # }
    #
    # born_location = forms.ModelChoiceField(
    #       queryset=Location.objects.all(),
    #      widget=autocomplete.ModelSelect2(url='location-autocomplete')
    #  )


admin.site.register(User, UserAdmin)
admin.site.register(Location)
admin.site.register(Country)
