from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def create_student(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is not None:
            try:
                stu=Student.objects.get(id=id)
            except:
                return Response({'msg':'Invalid id '})
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            return Response(serializer.data)
        
    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data saved successfully"})
        return Response(serializer.errors)
    
    if request.method=="PATCH":
        id=pk
        try:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu,request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':"Partial Data Updation Successfull!"})
        except:
            return Response({"msg":"Invalid ID"})
        
    if request.method=="PUT":
        id=pk
        try:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu,request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Complete data updation successfull !"})
        except:
            return Response({'msg':"Invalid id "})
        return Response(serializer.errors)
        
    if request.method=="DELETE":
        id=pk
        try:
            stu=Student.objects.get(id=id)
            stu.delete()
            return Response({"msg":"Data deletion Successfull!!"})
        except:
            return Response({'msg':"Invalid id"})
        