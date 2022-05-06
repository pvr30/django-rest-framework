from django import views
from django.db import router
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('studentapi', StudentModelViewSet, basename='student')




