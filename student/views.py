from rest_framework import viewsets

from student.models import Student
from student.serializers import StudentSerializer



class StundesViewSet(viewsets.ModelViewSet):
    """Return all students."""
    serializer_class = StudentSerializer

    queryset = Student.objects.all()
