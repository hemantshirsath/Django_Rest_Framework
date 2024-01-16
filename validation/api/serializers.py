from rest_framework import serializers
from .models import Student


def starts_with_r(value):
    if value[0]=='r':
        raise serializers.ValidationError('Intial must be capital')
    
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(validators=[starts_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField()

    def create(self,validated_data):
       return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    # def validate_roll(self,value):
    #     if value>=200:
    #         raise serializers.ValidationError('Seats Full')
    #     return value
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='gaurav' and ct.lower()!='jalgaon':
            raise serializers.ValidationError('City Must be Jalgaon')
        return data