from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response

# Create your views here.

# viewsets 

class StudentViewSet(ViewSet):
    
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Created'})
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
       student = Student.objects.get(id=pk)
       serializer = StudentSerializer(student)
       return Response(serializer.data)


    def update(self, request, pk=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Updated'})
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'msg': 'Successfully Deleted'})




# ModelViewSet
class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# ReadOnlyModelViewSet
# only get list and detail 
class StudentReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


