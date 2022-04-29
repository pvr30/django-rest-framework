from django.urls import path
from .views import *

urlpatterns = [
    # path('students/', students),
    path('students/', StudentAPI.as_view()),
    
]