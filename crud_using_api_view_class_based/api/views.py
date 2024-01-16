from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
# Create your views here.
class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        if pk is not None:
            try:
                stu=Student.objects.get(id=pk)
                serializer=StudentSerializer(stu)
                return Response(serializer.data)
            except:
                return Response({'msg':'Invalid ID'})
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            return Response(serializer.data)
        
    def post(self,request,pk=None,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data saved successfully!!"})
        return Response(serializer.errors)
    
    def patch(self,request,pk=None,format=None):
        try:
            stu=Student.objects.get(id=pk)
        except:
            return Response({'msg':"Invalid id"})
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':"Partial data updated successfully!!"})
        return Response(serializer.errors)
    def put(self,request,pk=None,format=None):
        try:
            stu=Student.objects.get(id=pk)
        except:
            return Response({'msg':"Invalid ID"})
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Full data updation Successfull!!"})
        return Response(serializer.errors)
    
    def delete(self,request,pk=None,format=None):
        try:
            stu=Student.objects.get(id=pk)
        except:
            return Response({'msg':"Invalid ID"})
        stu.delete()
        return Response({'msg':"Data deleted Successfully!!"})