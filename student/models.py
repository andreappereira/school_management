from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    document = models.CharField(max_length=14, blank=False, null=False, unique=True)
    date_of_birth = models.DateField(blank=False, null=False)
    active = models.BooleanField(blank=False, null=False, default=True)
    cellphone = models.CharField(max_length=11, null=True, default=None)
    photography = models.ImageField(blank=True)

    def __str__(self) -> str:
        return self.name
