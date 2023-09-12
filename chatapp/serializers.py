from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = '__all__' 

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()

