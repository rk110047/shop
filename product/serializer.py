from rest_framework import serializers
from .models import Product,Categories
from shopkeeper.serializer import ShopDetailSerializer





class ProductSerializer(serializers.ModelSerializer):
    url             =   serializers.HyperlinkedIdentityField(view_name='product:detail product',lookup_field='product_id')
    shop_name       =    ShopDetailSerializer(read_only=True)
    class Meta:
        model   =   Product
        fields  =   ['user','product_image','product_name','product_price','description','shop_name','url']
        read_only_fields    =   ['shop_name']



class ProductDetailSerializer(serializers.ModelSerializer):
    add_to_cart          =    serializers.HyperlinkedIdentityField(view_name='cart:add_to_cart',lookup_field='product_id')
    remove_from_cart     =    serializers.HyperlinkedIdentityField(view_name='cart:remove_from_cart',lookup_field='product_id')
    shop_name            =    ShopDetailSerializer(read_only=True)
    class Meta:
        model   =   Product
        fields  =   ['product_image','add_to_cart','product_name','product_price','description','shop_name','remove_from_cart']
        # read_only_fields    =   ['product_id','user','shop_name']



class ProductDetailForCartSerializer(serializers.ModelSerializer):
    # add_to_cart     =    serializers.HyperlinkedIdentityField(view_name='cart:add_to_cart',lookup_field='product_id')
    # shop_name       =    ShopDetailSerializer(read_only=True)
    class Meta:
        model   =   Product
        fields  =   '__all__'
        # read_only_fields    =   ['product_id','user','shop_name']


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Product
        fields  =   '__all__'
        read_only_fields    =   ['product_id','user','shop_name']



class ProductListOfUserSerializer(serializers.ModelSerializer):
    url             =   serializers.HyperlinkedIdentityField(view_name='product:detail of product',lookup_field='product_id')
    shop_name       =    ShopDetailSerializer(read_only=True)
    class Meta:
        model   =   Product
        fields  =   ['user','product_image','product_name','product_price','description','shop_name','quantity','url']
        read_only_fields    =   ['shop_name']

class ProductDetailForListSerializer(serializers.ModelSerializer):
    edit                 =      serializers.HyperlinkedIdentityField(view_name="product:edit product",lookup_field="product_id")
    shop_name            =    ShopDetailSerializer(read_only=True)
    delete               =      serializers.HyperlinkedIdentityField(view_name="product:delete product",lookup_field="product_id")

    class Meta:
        model   =   Product
        fields  =  ['user','product_code','quantity','product_image','product_name','product_price','description','shop_name',"Category",'active','edit','delete']
        # read_only_fields    =   ['product_id','user','shop_name']


class ProductUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   =   Product
        fields  =   '__all__'
        read_only_fields    =   ['product_id','user','shop_name']

class CreateCatSerializer(serializers.ModelSerializer):
    class Meta:
        model    =   Categories
        fields   =   "__all__"


