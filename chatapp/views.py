from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .serializers import RegistrationSerializer,LoginSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions,authentication
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.authtoken.models import Token 
import json
from .models import OnlineUsers

class UserRegistrationAPIview(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes=[]
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['username']
            password=serializer.validated_data['password']

            if User.objects.filter(username=email).exists():
                return Response({'message':'Email already exists'},status=status.HTTP_400_BAD_REQUEST)
            
            user=User.objects.create(username=email)
            user.set_password(password)
            user.save()
            return Response({'message':'Registration Successfull'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginAPIview(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes=[]
    
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']

            user = authenticate(username=email,password=password)
            if user:
                data={}
                login(request,user)
                token,_=Token.objects.get_or_create(user=user)
                name=email.split('@')[0]
                OnlineUsers.objects.create(name=name)
                data['token']=token.key
                return Response(data,status=status.HTTP_200_OK)
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserOnlineUsersAPIview(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes=[permissions.IsAuthenticated]

    def get(self,request):
        online_users=OnlineUsers.objects.all()
        online_users_list=[user.name for user in online_users]
        return Response(online_users_list)


class SuggestedFriendsAPIview(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request,id):
        with open("users.json", "r") as f:
            data=json.load(f)
            users = data.get('users', [])
            s_user = next((u for u in users if u['id'] == id), None)
            recommend_user=[user for user in users if s_user["age"]==user["age"]]
            if s_user:
                return Response(recommend_user[:5])
            
class StartAPIview(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes=[permissions.IsAuthenticated]

    def post(self,request):
        name=request.data
        username=name.get('username')
        online_users=OnlineUsers.objects.filter(name=username).first()
        if online_users:
            return Response({"message":"Successfull"})
        else:
            return Response({"message":"Not Successfull"})


def home1(request, group_name):
    return render(request, 'index2.html', {'group_name':group_name})