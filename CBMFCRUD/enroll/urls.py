from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_show, name='add'),
    path('update<int:id>', views.update_data, name='update'),
    path('delete<int:id>', views.delete_data, name='delete'),
]