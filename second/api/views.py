from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.http import JsonResponse
from .serializers import StudentSerializer

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def create_student(request):
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            data={
                'msg':"Data saved successfully"
            }
            return JsonResponse(data)
        return JsonResponse(serializer.errors)