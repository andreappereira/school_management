from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets, generics, filters

from registration.models import Registration
from registration.serializers import ListRegistrationStudentSerializer, ListStudentsEnrolledInTheCourseSerializer, RegistrationSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    """Return all registrations."""
    http_method_names = ['get', 'post', 'put']
    serializer_class = RegistrationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['student']
    filterset_fields = ['active', 'period']

    queryset = Registration.objects.all()

    @method_decorator(cache_page(50))
    def dispatch(self, request, *args, **kwargs):
        return super(RegistrationViewSet, self).dispatch(*args, **kwargs)
   

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
