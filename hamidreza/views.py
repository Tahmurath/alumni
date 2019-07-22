from django.http import HttpResponse
from students.models import Student
from django.shortcuts import render


def index(request):
    num_students = Student.objects.all().count();

    context = {
        'num_students': num_students,
    }

    return render(request, 'index.html', context=context)
    #return HttpResponse("Hello, world. You're at the hamidreza index.")