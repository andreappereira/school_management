from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from student.models import Student
from student.serializers import StudentSerializer



class StundesViewSet(viewsets.ModelViewSet):
    """Return all students."""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = StudentSerializer

    queryset = Student.objects.all()
