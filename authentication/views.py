from django.shortcuts import render
from .serializer import RegisterSerializer,LoginSerializer
from rest_framework import generics,mixins,status
from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate,login
from rest_framework_jwt.settings import api_settings
from utils.permissions import NonRegisteredUserOnly

jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
jwt_payload_response_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER





class LoginAPIView(generics.GenericAPIView):
    serializer_class    =       LoginSerializer
    permission_classes     =   [NonRegisteredUserOnly]
    authentication_classes =   []

    def post(self,request):
        print(request.data)
        username    =   request.data.get('username')
        password    =   request.data.get('password')
        print(username)
        print(password)
        user        =   authenticate(username=username,password=password)
        print(user)
        if user is not None:
            payload     = jwt_payload_handler(user)
            token       = jwt_encode_handler(payload)
            login(request,user)
            response = jwt_payload_response_handler(token,user,request=request)
            return Response(response, status=status.HTTP_200_OK)
        response = {
        "data": {
            "message": "Your login information is invalid",
            "status": "invalid"
        }
    }
        return Response(response, status=status.HTTP_200_OK)





class RegisterAPIView(generics.CreateAPIView):
     queryset               =   User.objects.all()
     permission_classes     =   [NonRegisteredUserOnly]
     authentication_classes =   []
     serializer_class       =   RegisterSerializer
