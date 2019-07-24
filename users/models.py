from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    location_title = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.location_title


class Country(models.Model):
    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    country_title = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.country_title


class User(AbstractUser):
    # class Meta:
    #     db_table = 'auth_user'

    GENDER_TYPE_CHOICES = (
        ('m', _('Male')),
        ('f', _('Female')),
        ('o', _('Other'))
    )

    MARITAL_TYPE_CHOICES = (
        ('unmarried', _('Unmarried')),
        ('married', _('Married')),
        ('divorced', _('Divorced')),
        ('widowed', _('Widowed')),
        ('separated', _('Separated')),
        ('o', _('Other'))
    )

    PHYSICAL_TYPE_CHOICES = (
        ('healthy', _('Healthy')),
        ('deaf', _('Deaf')),
        ('blind', _('Blind')),
        ('disabled', _('Disability Movement')),
        ('o', _('Other'))
    )

    ISARGARI_TYPE_CHOICES = (
        ('farzand_shahid', _('Farzand Shahid')),
        ('farzand_azadeh', _('Farzand Azadeh')),
        ('farzand_janbaz', _('Farzand Janbaz')),
        ('farzand_razmandeh', _('Farzand Razmandeh')),
        ('farzand_javidasar', _('Farzand Javidasar')),
        ('hamsar_shahid', _('Hamsar Shahid')),
        ('hamsar_azadeh', _('Hamsar Azadeh')),
        ('hamsar_janbaz', _('Hamsar Janbaz')),
        ('hamsar_razmandeh', _('Hamsar Razmandeh')),
        ('hamsar_javidasar', _('Hamsar Javidasar')),
        ('janbaz', _('Janbaz')),
        ('azadeh', _('Azadeh')),
        ('razmandeh', _('Razmandeh')),
        ('o', _('Other'))
    )

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    first_name = models.CharField(_('first name'), max_length=30, )
    last_name = models.CharField(_('last name'), max_length=150, )

    person_shen_number = models.CharField(_('Shenasname Code'), max_length=32, blank=True, null=True)
    person_melli_code = models.CharField(_('Melli Code'), max_length=32)
    person_gender = models.CharField(_('Gender'), max_length=16, choices=GENDER_TYPE_CHOICES, )
    person_father_name = models.CharField(_('Father Name'), max_length=100, null=True, blank=True, )
    person_born_date = models.DateField(_('Birthday'), default=date.today, blank=True)
    email = models.EmailField(_('Email'), max_length=100, blank=True, default='0')
    nation = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Nation'),
                               related_name="nationality")
    # nation_id = models.IntegerField(default='0',blank=True)
    born_location = models.ForeignKey(Location, default=1, on_delete=models.CASCADE, blank=True,
                                      related_name="born_place")
    # country_id = models.IntegerField(default='0', blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Country'),
                                related_name="home_country")
    city = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('City'),
                             related_name='home_city')
    # city_id = models.IntegerField(default='0', blank=True)
    mobile_number = models.CharField(_('Mobile Number'), max_length=100, blank=True, null=True)
    phone_number = models.CharField(_('Phone Number'), max_length=100, blank=True, null=True)
    postal_code = models.CharField(_('Postal Code'), max_length=100, blank=True, null=True)
    person_address = models.CharField(_('Address'), max_length=500, blank=True, null=True)
    sajad_person_id = models.IntegerField(_('Sajad Person ID'), default='0', blank=True)

    isargari = models.CharField(_('Isargar'), choices=ISARGARI_TYPE_CHOICES, max_length=500, blank=True, null=True)

    military = models.CharField(_('Military'), choices=ISARGARI_TYPE_CHOICES, max_length=500, blank=True, null=True)

    marital_status = models.CharField(_('Marital Status'), choices=MARITAL_TYPE_CHOICES, max_length=500, blank=True,
                                      null=True)
    physical_condition = models.CharField(_('Physical Condition'), choices=PHYSICAL_TYPE_CHOICES, max_length=500,
                                          blank=True, null=True)
    number_of_children = models.IntegerField(_('Number of Children'), blank=True, null=True)
    avatar = models.ImageField( upload_to="user/%Y/%m/%d/")
    # null=True, blank=True,

    def getUserHash(self):
        import hashlib
        import datetime
        x = datetime.datetime.now()
        str1 = str(self.last_name)
        str2 = str(self.id)
        str3 = x.strftime("%Y-%m-%d")
        str4 = str1 + str2 + str3

        return hashlib.md5(str4.encode('utf-8')).hexdigest()

    def __str__(self):
        return self.get_full_name()

    # def getGender(self):
    #     for x, y in self.GENDER_TYPE_CHOICES:
    #         if self.person_gender == x:
    #             return y


class Sabteahval(models.Model):
    class Meta:
        verbose_name = _('Sabteahval')
        verbose_name_plural = _('Sabteahvals')

    first_name = models.CharField(_('first name'), max_length=30, )
    last_name = models.CharField(_('last name'), max_length=150, )
    person_father_name = models.CharField(_('Father Name'), max_length=100, null=True, blank=True, )
    person_shen_number = models.CharField(_('Shenasname Code'), max_length=32, blank=True, null=True)
    person_born_date = models.CharField(_('Birthday'), max_length=32, blank=True, null=True)
    person_melli_code = models.CharField(_('Melli Code'), max_length=32)
    mobile_number = models.CharField(_('Mobile Number'), max_length=100, blank=True, null=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('User'))

    def __str__(self):
        # full_name = '%s %s' % (self.first_name, self.last_name)
        return self.first_name + " " + self.last_name
