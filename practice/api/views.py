from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST','PUT','PATCH',''])
def StudentAPI(request,id=None):
