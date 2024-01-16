from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    age=serializers.IntegerField()
    city=serializers.CharField()