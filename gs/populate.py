import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','gs.settings')
import django
django.setup()

from fbcbv.models import *
from faker import Faker
from random import *
faker = Faker()
def populate(n):
    for i in range(n):
        feno = randint(1001,9999)
        fename = faker.name()
        fesal=randint(10000,40000)
        feaddr=faker.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,
                                                  eaddr=feaddr)

populate(30)