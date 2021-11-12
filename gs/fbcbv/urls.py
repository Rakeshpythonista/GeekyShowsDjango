from django.urls import path
from . import views

urlpatterns = [
    path('views/', views.Myview.as_view(), name='views'),
]
