from django.db import models


# Create your models here.
class Course(models.Model):
    class courseLevel(models.IntegerChoices):
        BASIC = 0, 'Basic',
        MEDIUM = 1, 'Medium',
        ADVANCED = 2, 'Advanced'

    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    level  = models.IntegerField(choices=courseLevel.choices, blank=False, null=False)

    def __str__(self) -> str:
        return self.description
