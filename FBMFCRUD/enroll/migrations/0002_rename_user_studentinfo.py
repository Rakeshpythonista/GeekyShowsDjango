# Generated by Django 3.2.8 on 2021-11-03 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='StudentInfo',
        ),
    ]