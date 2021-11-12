from django.shortcuts import render
from .models import Employee


# Create your views here.
def employee_info(request):
    employees = Employee.objects.all()
    empsal = Employee.objects.filter(esal__lt=30000)
    return render(request, 'orm/orm.html',
                  {'employees': employees,
                   'empsal': empsal})
