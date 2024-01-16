from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView
from .pagination import MyCursorPagination

# Create your views here.
class StudentAPI(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyCursorPagination