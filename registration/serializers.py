from rest_framework import serializers

from registration.models import Registration
from registration.validators import *


class RegistrationSerializer(serializers.ModelSerializer):
    def validate(self, data):
  
        if validate_existing_registration(data['student'], data['course'], data['period']):
            raise serializers.ValidationError("This registration already exists.")

        return data
    
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
        