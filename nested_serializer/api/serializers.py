from rest_framework import serializers
from .models import Singer,Song

class SingerSerializer(serializers.ModelSerializer):
    song=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Singer
        fields=['id','name','gender','song']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=['id','title','singer']