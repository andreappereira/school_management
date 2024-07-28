from django.db import models

from course.models import Course
from student.models import Student


# Create your models here.
class Registration(models.Model):
    class Period(models.IntegerChoices):
        MORNING = 0, 'Morning',
        AFTERNOON  = 1, 'Afternoon'
        NIGHT = 2, 'Night'

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.IntegerField(choices=Period.choices, blank=False, null=False)
    active = models.BooleanField(blank=False, null=False, default=True)
