from rest_framework import serializers

from course.models import Course


class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
