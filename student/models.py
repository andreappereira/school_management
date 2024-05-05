from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    document = models.CharField(max_length=14, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)

    def __str__(self) -> str:
        return self.name
