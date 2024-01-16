from django.shortcuts import render,HttpResponse
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
# Create your views here.
from .models import Student
def view_student(request,pk):
    try:
        stu=Student.objects.get(pk=pk)
    except:
        return HttpResponse({'404 not found'},content_type='application/json')
    print(stu)
    serializer=StudentSerializer(stu)
    response=JSONRenderer().render(serializer.data)
    return HttpResponse(response,content_type="application/json")

def viewall(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    response=JSONRenderer().render(serializer.data)
    return HttpResponse(response,content_type='application/json')
    