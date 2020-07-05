from django.shortcuts import render
from rest_framework import generics
from .models import DeliveryPersonProfile
from .serializer import DeliveryPersonDetailSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response


class DeliveryPersonProfileAPIView(generics.GenericAPIView):
	queryset					=		DeliveryPersonProfile.objects.all()
	authentication_classes		=		[SessionAuthentication,JSONWebTokenAuthentication]
	permission_classes			=		[]
	serializer_class			=		DeliveryPersonDetailSerializer



	def get(self,request,*args,**kwargs):
		try:
			user			=		self.request.user
			profile 		=		DeliveryPersonProfile.objects.get(user=user)
			serializer      =		DeliveryPersonDetailSerializer(profile)
			return Response(serializer.data)
		except:
			return Response({"message":"No profile exist"})
