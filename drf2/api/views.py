from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.

@csrf_exempt
def students(request):

    # get
    if request.method == 'GET':
        data = request.body
        stream = io.BytesIO(data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    # post
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg": "successfully added"})
        return JsonResponse(serializer.errors)

    # put/update
    if request.method == 'PUT':
        data = request.body
        stream = io.BytesIO(data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg": "successfully updated"})
        return JsonResponse(serializer.errors)

    # delete
    if request.method == 'DELETE':
        data = request.body
        stream = io.BytesIO(data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return JsonResponse({"msg": "successfully deleted"})
        except:
            return JsonResponse({"msg": "object does not exist"})



# class based
@method_decorator(csrf_exempt, name="dispatch")
class StudentAPI(View):

    def get(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)


    def post(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg": "successfully added"})
        return JsonResponse(serializer.errors)

    def put(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg": "successfully updated"})
        return JsonResponse(serializer.errors)

    def delete(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return JsonResponse({"msg": "successfully deleted"})
        except:
            return JsonResponse({"msg": "object does not exist"})
