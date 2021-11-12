from django.contrib import admin
from .models import Page,Post, Songs


# Register your models here.
@admin.register(Page)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'page_name', 'page_cat', 'page_publish_date']


@admin.register(Post)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post_name', 'post_cat', 'post_publish_date']


@admin.register(Songs)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration']