from django.shortcuts import render
from .models import Employee
from django.views.generic.base import TemplateView


# class based view, by default get method not works.
class Myview(TemplateView):
    template_name = 'relation/relation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['details'] = Employee.objects.all()
        return context
