from rest_framework import serializers

from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'document',
            'date_of_birth',
            'photography'
        ]

class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'document',
            'date_of_birth',
            'photography',
            'cellphone',
        ]
