from django.contrib import admin
from students.models import Student, Field, Center, Military, Term
from .forms import StudentForm





class StuentAdmin(admin.ModelAdmin):
    form = StudentForm




# Register your models here.
admin.site.register(Student, StuentAdmin)
admin.site.register(Field)
admin.site.register(Term)
admin.site.register(Center)
admin.site.register(Military)

