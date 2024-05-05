from rest_framework import serializers

from registration.models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class ListRegistrationStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    def get_period(self, object):
        return object.get_period_display()

    class Meta:
        model = Registration
        fields = [
            'course',
            'period'
        ]

class ListStudentsEnrolledInTheCourseSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Registration
        fields = [
            'student'
        ]