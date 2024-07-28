from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from registration.models import Registration
from registration.serializers import ListRegistrationStudentSerializer, ListStudentsEnrolledInTheCourseSerializer, RegistrationSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    """Return all registrations."""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = RegistrationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['student']
    filterset_fields = ['active', 'period']

    queryset = Registration.objects.all()

class ListRegistrationStudent(generics.ListAPIView):
    """Return all registrations of student."""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ListRegistrationStudentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        queryset = Registration.objects.filter(student_id=pk)
        return queryset
    
class ListStudentsEnrolledInTheCourse(generics.ListAPIView):
    """Return all registration students in the course."""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ListStudentsEnrolledInTheCourseSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        queryset = Registration.objects.filter(course_id=pk)
        return queryset
