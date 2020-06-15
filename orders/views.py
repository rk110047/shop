from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from .serializer import OrderDetailSerializer
from rest_framework.response import Response
from .models import Order
from cart.models import Cart,OrderItem
from .models import Order

SessionAuthentication

class OrdersAPIView(generics.ListAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[SessionAuthentication]



	def get_queryset(self):
		request 	        =	self.request
		billing_profile		=	request.user.billingprofile
		queryset			=	Order.objects.filter(billing_profile=billing_profile)
		return queryset




class PlaceOrder(generics.GenericAPIView):
	queryset		    		= 		[]
	serializer_class			=		[]
	permission_classes  		=    	[]
	authentication_classes		=		[SessionAuthentication]


	def get(self,request):
		request				=	self.request
		user 				=   request.user
		billing_profile     =   user.billingprofile
		qs 					=	Cart.objects.filter(User=user,active=True)
		try:
			qs                  =   qs.first()
			qs.active			=	False
			qs.save()
		except:
			print(qs)	
		qs1         		=   OrderItem.objects.filter(User=user,active=True)
		try:
			for x in qs1:
				x.active		=	False
				x.save()
		except:
			print(qs1)
		qs2					=	Order.objects.filter(billing_profile=billing_profile,active=True,ordered=False)
		try:
			qs2                  =   qs2.first()
			qs2.ordered         =   True
			qs2.save()
		except:
			print(qs2)
		return Response("ok")



