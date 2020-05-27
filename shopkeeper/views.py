from django.shortcuts import render
from rest_framework import generics
from .models import ShopProfile
from .serializer import ShopProfileCreateSerializer,ShopsSerializer
from rest_framework.authentication import SessionAuthentication

class ShopProfileCreateAPIView(generics.CreateAPIView):
    queryset                =   ShopProfile
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    serializer_class        =   ShopProfileCreateSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class ShopsAPIView(generics.ListAPIView):
	authentication_classes  =   []
	serializer_class        =   ShopsSerializer
	permission_classes      =   []
	def get_queryset(self,*args,**kwargs):
		shops = ShopProfile.objects.filter(active=True)
		return shops


