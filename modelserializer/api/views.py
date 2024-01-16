from django.shortcuts import render,HttpResponse
from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
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
            jsonr=JSONRenderer().render({'msg':'Data created successfully'})
            return HttpResponse(jsonr,content_type='application/json')
        jsonr=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsonr,content_type='application/json')

    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        try:
            stu=Student.objects.get(id=id)
        except:
            data={'msg':"Invalid ID"}
            data=JSONRenderer().render(data)
            return HttpResponse(data,content_type='application/json')
        serializer=StudentSerializer(stu,pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':"Data updated successfully"})
        return JsonResponse(serializer.errors,safe=False)
    
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        try:
            stu=Student.objects.get(id=id)
            stu.delete()
            return JsonResponse({'msg':'Data deleted successfully'})
        except:
            return JsonResponse({'data':"invalid id"})
        