from django.urls import path
from .views import *


urlpatterns = [
   path('studentapi', LCStudentAPI.as_view()),
   path('studentapi/<int:pk>', StudentAPI.as_view()),
]