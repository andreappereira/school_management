import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

import random
from student.models import Student
from course.models import Course
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

        student = Student(name=name, document=document, date_of_birth=date_of_birth, active=active)
        student.save()

def create_courses(quantity):
    for _ in range(quantity):
        names = ['Python Fundamentos', 'Python intermediário','Python Avançado', 'Python para Data Science', 'Python/React']

        name = random.choice(names)
        description = name
        level = random.choice([Course.courseLevel.ADVANCED, Course.courseLevel.BASIC, Course.courseLevel.MEDIUM])
        names.remove(name) 

        course = Course(name=name, description=description, level=level)
        course.save()

create_students(50)
create_courses(5)
print('Created!')