from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from course.models import course
from course.serializers import courseSerializer


class coursesViewSet(viewsets.ModelViewSet): 
    """Return all courses."""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = courseSerializer

    queryset =  course.objects.all()
