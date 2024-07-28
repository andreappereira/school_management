from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from student.models import Student
from student.serializers import StudentSerializer, StudentSerializerV2


class StundesViewSet(viewsets.ModelViewSet):
    """Return all students."""

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['name']
    search_fields = ['name', 'document']
    filterset_fields = ['active']
    
    queryset = Student.objects.all()

    def get_serializer_class(self):
        return StudentSerializerV2 if self.request.version == 'v2' else StudentSerializer
