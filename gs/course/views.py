from django.shortcuts import render
from .models import Student
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def studinfo(request):
    students = Student.objects.all()
    return render(request, 'course/courses.html', {'students': students})
