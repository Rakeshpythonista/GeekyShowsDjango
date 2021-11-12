from django.urls import path
from . import views

urlpatterns = [
    path('empinfo/', views.employee_info, name='empinfo'),
]