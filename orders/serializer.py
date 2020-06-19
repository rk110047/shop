from rest_framework import serializers
from .models import Order
from addresses.serializer import AddressSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from cart.serializer import CartDetailforOrderSerializer,OrderItemDetailSerializer,CartDetailSerializer
from product.serializer import ProductDetailSerializer 



class OrderDetailSerializer(WritableNestedModelSerializer):

	cart = CartDetailforOrderSerializer()
	billing_address= AddressSerializer()
	shipping_address=AddressSerializer()
	class Meta:
		model 		= Order
		fields 		= "__all__"