from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from .models import Student
import io
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def view_student(request):
    if request.method=="GET":
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            data={
                'msg':"data saved successfully"
            }
            return JsonResponse(data,safe=False)
        return JsonResponse(serializer.errors,safe=False)
    
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            data={
                'msg':'data Updated successfully'
            }
            return JsonResponse(data,safe=False)
        return JsonResponse(serializer.errors,safe=False)
    
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        try:
            stu=Student.objects.get(id=id)
        except:
            return JsonResponse({
                'msg':"invalid id"
            })
        if stu is not None:
            stu.delete()
            data={
                'msg':"data deleted successfully"
            }
            return JsonResponse(data,safe=False)
        
