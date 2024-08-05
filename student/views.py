from django.shortcuts import render
from .serializers import StudentSerializer,SubjectSerializer,StudentSubjectSerializer,\
    StudentSubjectGetSerializer, StudentSubjectUpdateSerializer
from .models import Student,Subject,StudentSubject
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view(['GET','POST',"PUT","DELETE"])
# def student(request):
#     if request.method == "GET":
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)
#     elif request.method== "POST":
#         # breakpoint()
#         stu=request.data
        
#         serializer=StudentSerializer(data=stu)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)


## using generics apiview

from rest_framework import generics, viewsets

class StudentApiView(generics.ListCreateAPIView):
    """
    StudentApiView for performing CRUD opretatiuon for Student Data
    argekj:
    
        First_name:first_name should start with M   
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# from rest_framework import generics, viewsets

class StudentUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    StudentApiView for performing CRUD opretatiuon for Student Data
    argekj:
    
        First_name:first_name should start with M   
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class SubjectRetriveCreate(generics.RetrieveUpdateDestroyAPIView):
    
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer

class SubjectCreate(generics.CreateAPIView):
    
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer


class StudentSubjectAPI(viewsets.ModelViewSet):
    
    queryset=StudentSubject.objects.all()
    serializer_class=StudentSubjectSerializer

    def get_serializer_class(self):
        if self.request.method=="GET":
            return StudentSubjectGetSerializer
        if self.request.method in ["PUT","PATCH"]:
            return StudentSubjectUpdateSerializer
        return super().get_serializer_class()

