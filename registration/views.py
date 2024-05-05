from rest_framework import viewsets, generics

from registration.models import Registration
from registration.serializers import ListRegistrationStudentSerializer, ListStudentsEnrolledInTheCourseSerializer, RegistrationSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    """Return all registrations."""
    serializer_class = RegistrationSerializer

    queryset = Registration.objects.all()

    
class ListRegistrationStudent(generics.ListAPIView):
    """Return all registrations of student."""
    serializer_class = ListRegistrationStudentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Registration.objects.filter(student_id=pk)

        return queryset


class ListStudentsEnrolledInTheCourse(generics.ListAPIView):
    """Return all registration students in the course."""

    serializer_class = ListStudentsEnrolledInTheCourseSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        queryset = Registration.objects.filter(course_id=pk)

        return queryset



