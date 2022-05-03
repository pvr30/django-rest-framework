from functools import partial
from .models import Student
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


# function based api view
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Created'})
        return Response(serializer.errors)


    if request.method == 'PUT':
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Updated'})
        return Response(serializer.errors)


    if request.method == 'DELETE':
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'msg': 'Successfully Deleted'})


# class based view
class StudentAPI(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Created'})
        return Response(serializer.errors)

    def put(self, request, pk=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'msg': 'Successfully Deleted'})

