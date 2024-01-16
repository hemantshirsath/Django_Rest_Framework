from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    city=serializers.CharField()

    def create(self,validate_data):
        return Student.objects.create(**validate_data)
