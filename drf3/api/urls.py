from django.urls import path
from .views import *


urlpatterns = [
    path('studentapi/', student),
    path('studentapi/<str:pk>', student),


    path('studentapi/', StudentAPI.as_view()),
    path('studentapi/<str:pk>', StudentAPI.as_view()),
]