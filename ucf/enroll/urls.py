from django.urls import path
from . import views
from django.views.generic import VI

urlpatterns = [
    path('', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
]
