from django.shortcuts import render
from rest_framework import generics
from .models import ShopProfile
from django.db.models import Q
from .serializer import ShopProfileCreateSerializer,ShopsSerializer,ShopProfileDetailSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

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

	def get_queryset(self):
		request 	= 	self.request
		queryset    =	ShopProfile.objects.filter(active=True)
		query       =   request.GET.get('q')
		if query is not None:
			queryset 		= 	queryset.filter(Q(shop_name__icontains=query))
			# return shops
		return queryset

class ShopProfileDetailAPIView(generics.GenericAPIView):
    queryset                =   ShopProfile
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    serializer_class        =   ShopProfileDetailSerializer

    def get(self,request):
        user 			= 		request.user
        shopProfile     =		ShopProfile.objects.get(user=user)
        serialize  		=		ShopProfileDetailSerializer(shopProfile,context={'request': request})
        return Response(serialize.data)

class ShopProfileEditAPIView(generics.UpdateAPIView):
	queryset                =   ShopProfile
	permission_classes      =   []
	authentication_classes  =   []
	serializer_class        =   ShopProfileCreateSerializer
	lookup_field			=		"id"

