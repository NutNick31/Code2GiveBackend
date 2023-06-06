from rest_framework import serializers
from .models import UserInfoModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfoModel
        fields = ['id', 'email', 'username', 'college', 'location']
