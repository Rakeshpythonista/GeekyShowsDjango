from django.shortcuts import render
from .models import Page


# Create your views here.
def dbrelation(request):
    pages = Page.objects.all()
    return render(request, 'relation/relation.html', {'pages': pages})
