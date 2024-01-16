from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListCreateAPIView
# from .pagination import MyPageNumberPagination
# Create your views here.
class StudentApi(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # pagination_class=MyPageNumberPagination
    
