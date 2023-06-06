from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import UserInfoModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = UserInfoModel.objects.all()
    serializer_class = MyModelSerializer
