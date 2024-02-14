from rest_framework import serializers
from .models import Singer,Song

class SongSerializer(serializers.ModelSerializer):
    singer_name = serializers.CharField(source='singer.name', read_only=True)
    class Meta:
        model=Song
        fields=['id','title','singer','singer_name']
    
class SingerSerializer(serializers.ModelSerializer):
    # song=serializers.StringRelatedField(many=True,read_only=True)
    # song=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    song=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    # song=serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    class Meta:
        model=Singer
        fields=['id','name','song','gender']