from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@permission_classes([IsAdminUser])
@authentication_classes([BasicAuthentication])
def StudentAPI(request,id=None):
    if request.method=="GET":
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
        
    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data saved successfully!!"})
        return Response(serializer.errors)

    if request.method=="PATCH":
        if id is not None:
            try:
                stu=Student.objects.get(id=id)
            except:
                return Response({'msg':"Invalid ID"})
            serializer=StudentSerializer(stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':"Partial data saved successfully"})
        
    if request.method=="PUT":
        if id is not None:
            try:
                stu=Student.objects.get(id=id)
            except:
                return Response({'msg':"Invalid ID"})
            serializer=StudentSerializer(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':"Full data updation successfull"})
            return Response(serializer.errors)
    
    if request.method=="DELETE":
        if id is not None:
            try:
                stu=Student.objects.get(id=id)
            except:
                return Response({'msg':"Invalid ID"})
            stu.delete()
            return Response({'msg':"Data deleted successfully!!"})

