from django.db import models

# Create your models here.


class Student(models.Model):
    std_code = models.CharField(max_length=200)
    center_name = models.CharField(max_length=11)
    center_id = models.CharField(max_length=11)
    field_name = models.CharField(max_length=11)
    field_id = models.CharField(max_length=11)
    graduate_date = models.CharField(max_length=11)
    enter_year = models.CharField(max_length=11)
