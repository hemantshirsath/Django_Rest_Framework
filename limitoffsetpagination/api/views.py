from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import StudentSerializer
# from .pagination import MyLimitOffsetPagination
from .models import Student
# Create your views here.
class StudentAPI(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # pagination_class=MyLimitOffsetPagination
