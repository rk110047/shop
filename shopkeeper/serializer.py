from rest_framework import serializers
from .models import ShopProfile
from authentication.user.serializer import UserDetailSerializer

class ShopProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       ShopProfile
        fields      =       '__all__'
        read_only_fields        =  ['user']



class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       ShopProfile
        fields      =       ['shop_name']

class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       ShopProfile
        fields      =       '__all__'
