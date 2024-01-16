from django.shortcuts import render
from .serializers import SongSerializer,SingerSerializer
from .models import Singer,Song
from rest_framework import viewsets
# Create your views here.
class SingerAPI(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer

class SongAPI(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer