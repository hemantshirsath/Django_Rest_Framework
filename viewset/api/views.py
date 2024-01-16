from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
# Create your views here.
class StudentAPI(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data saved successfully!!"})
        return Response(serializer.errors)
    
    def retrieve(self,request,pk):
        if pk is not None:
            try:
                stu=Student.objects.get(id=pk)
            except:
                return Response({'msg':"Invalid ID"})
            Serializer=StudentSerializer(stu)
            return Response(Serializer.data)
        
    def partial_update(self,request,pk):
        try:
            stu=Student.objects.get(id=pk)
            serializer=StudentSerializer(stu,request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Partial data updated succesfull!!'})
            return Response(serializer.errors)
        except:
            return Response({'msg':"Invalid ID"})

    def update(self,request,pk):
        try:
            stu=Student.objects.get(id=pk)
            serializer=StudentSerializer(stu,request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Full data updated succesfull!!'})
            return Response(serializer.errors)
        except:
            return Response({'msg':"Invalid ID"})
        
    def destroy(self,request,pk):
        try:
            stu=Student.objects.get(id=pk)
            stu.delete()
            return Response({'msg':"Data deleted successfully!!"})
        except:
            return Response({'msg':"Invalid id "})