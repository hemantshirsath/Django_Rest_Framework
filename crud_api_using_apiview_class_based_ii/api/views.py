from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentAPI(APIView):
    def get(self,request,format=None):
        id=request.data.get('id')
        if id is not None:
            try:
                stu=Student.objects.get(id=id)
            except:
                return Response({'msg':"Invalid ID"})
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            return Response(serializer.data)
     
        
    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data inserted !!"})
        return Response(serializer.errors)

    def put(self,request,format=None):
        id=request.data.get('id')
        try:
            stu=Student.objects.get(id=id)
        except:
            return Response({'msg':"Invalid ID"})
        serializer=StudentSerializer(stu,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data updated Successfully!!"})
        return Response(serializer.errors)

    def delete(self,request,format=None):
        id=request.data.get('id')
        try:
            stu=Student.objects.get(id=id)
        except:
            return Response({'msg':"Invalid ID"})
        stu.delete()
        return Response({'msg':"Data deleted Successfully!!"})
        

           