from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _


class Center(models.Model):

    class Meta:
        verbose_name = _('Center')
        verbose_name_plural = _('Centers')

    center_title = models.CharField(max_length=32, blank=True)
    center_code = models.IntegerField(blank=True)

    def __str__(self):
        return self.center_title


class Field(models.Model):

    class Meta:
        verbose_name = _('Field')
        verbose_name_plural = _('Fields')

    field_title = models.CharField(max_length=32, blank=True)
    field_code = models.IntegerField(blank=True)

    def __str__(self):
        return self.field_title


class Military(models.Model):

    class Meta:
        verbose_name = _('Military')
        verbose_name_plural = _('Military Types')

    military_title = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.military_title


class Term(models.Model):

    class Meta:
        verbose_name = _('Term')
        verbose_name_plural = _('Terms')

    term_title = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.term_title


class Student(models.Model):

    class Meta:
        permissions = (("can_see_all_students", "View all Students"),)
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('User'))
    center = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Center'))
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Field'))
    std_code = models.CharField(_('Student Code'), max_length=32, blank=True)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Term'))
    military = models.ForeignKey(Military, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Military Status'))
    start_date = models.CharField(_('Entry Date'), max_length=32, blank=True)
    stop_date = models.CharField(_('Graduate Date'), max_length=32, blank=True)

    def __str__(self):
        return self.person.get_full_name() + " " + self.center.center_title





