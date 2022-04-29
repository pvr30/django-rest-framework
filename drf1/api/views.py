import io
from .models import Student
from .serializer import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.


# get one student's details
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    data = serializer.data
    return JsonResponse(data)


# get a list of all objects/students
def students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)


# create object
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.validated_data)
        return JsonResponse(serializer.errors)
    
    