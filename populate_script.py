import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

import random
from student.models import Student
from course.models import course
from faker import Faker
from validate_docbr import CPF

fake = Faker('pt_BR')
Faker.seed(10)

def create_students(quantity):
    for _ in range(quantity):
        cpf = CPF()
        name = fake.name()
        document = cpf.generate()
        date_of_birth = fake.date_of_birth()
        active = random.choice([True, False])

        p = Student(name=name, document=document, date_of_birth=date_of_birth, active=active)
        p.save()

def create_courses(quantity):
    for _ in range(quantity):
        name = fake.name()
        description = fake.name()
        level = random.choice([course.courseLevel.ADVANCED, course.courseLevel.BASIC, course.courseLevel.MEDIUM])

        p = course(name=name, description=description, level=level)
        p.save()

create_students(50)
create_courses(50)
print('Created!')