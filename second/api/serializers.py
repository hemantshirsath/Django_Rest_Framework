from rest_framework import serializers
from .models import student
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    city=serializers.CharField()
    
    def create(self,validate_data):
        return student.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        
