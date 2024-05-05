from rest_framework import viewsets

from course.models import course
from course.serializers import courseSerializer


class coursesViewSet(viewsets.ModelViewSet): 
    """Return all courses."""
    serializer_class = courseSerializer

    queryset =  course.objects.all()
