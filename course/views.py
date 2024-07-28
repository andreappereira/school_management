from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from course.models import Course
from course.serializers import CourseSerializer


class coursesViewSet(viewsets.ModelViewSet): 
    """Return all courses."""
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['name']
    search_fields = ['name']
    filterset_fields = ['level']

    queryset =  Course.objects.all()
