from django.urls import path
from . import views

urlpatterns = [
    path('relations/', views.dbrelation, name='relations'),
]