from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from course.models import course
from course.serializers import courseSerializer


class coursesViewSet(viewsets.ModelViewSet): 
    """Return all courses."""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = courseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['name']
    search_fields = ['name']
    filterset_fields = ['level']

    queryset =  course.objects.all()
