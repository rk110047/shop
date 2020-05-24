from rest_framework import serializers
from .models import Product
from shopkeeper.serializer import ShopDetailSerializer




class ProductSerializer(serializers.ModelSerializer):
    url             =   serializers.HyperlinkedIdentityField(view_name='product:detail product',lookup_field='product_id')
    shop_name       =    ShopDetailSerializer(read_only=True)
    class Meta:
        model   =   Product
        fields  =   ['product_image','product_name','product_price','description','brand_name','shop_name','url']
        read_only_fields    =   ['user','shop_name']



class ProductDetailSerializer(serializers.ModelSerializer):
    add_to_cart          =    serializers.HyperlinkedIdentityField(view_name='cart:add_to_cart',lookup_field='product_id')
    remove_from_cart     =    serializers.HyperlinkedIdentityField(view_name='cart:remove_from_cart',lookup_field='product_id')
    shop_name            =    ShopDetailSerializer(read_only=True)
    class Meta:
        model   =   Product
        fields  =   ['product_image','add_to_cart','product_name','product_price','description','brand_name','shop_name','remove_from_cart']
        # read_only_fields    =   ['product_id','user','shop_name']



class ProductDetailForCartSerializer(serializers.ModelSerializer):
    # add_to_cart     =    serializers.HyperlinkedIdentityField(view_name='cart:add_to_cart',lookup_field='product_id')
    # shop_name       =    ShopDetailSerializer(read_only=True)
    class Meta:
        model   =   Product
        fields  =   '__all__'
        # read_only_fields    =   ['product_id','user','shop_name']
