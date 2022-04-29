from django.urls import path
from .views import student_create, student_detail, students

urlpatterns = [
    path('student/<int:pk>', student_detail),
    path('students/', students),
    path('student/create', student_create)

]