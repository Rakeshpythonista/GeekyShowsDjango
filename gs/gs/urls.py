from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('course.urls')),
    path('', include('student.urls')),
    path('', include('ormquery.urls')),
    path('', include('relation.urls')),
    path('', include('fbcbv.urls')),
]
