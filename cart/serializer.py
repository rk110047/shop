from rest_framework import serializers
from product.serializer import ProductDetailForCartSerializer
from .models import Cart
from .models import OrderItem

from product.serializer import ProductDetailSerializer


from drf_writable_nested.serializers import WritableNestedModelSerializer


class CartDetailSerializer(WritableNestedModelSerializer):
    # remove_from_cart     =    serializers.HyperlinkedIdentityField(view_name='cart:remove_from_cart',lookup_field='product_id')
    delete_item_from_cart = serializers.HyperlinkedIdentityField(view_name='cart:delete_item_from_cart',lookup_field='item_id')
    # url             =   serializers.HyperlinkedIdentityField(view_name='product:detail product',lookup_field='product_id')
    product         =   ProductDetailSerializer()
    # item              =   serializers.SerializerMethodField()
    class Meta:
        model      = OrderItem
        fields     = ["item_id",
                    "product",
                  "quantity",
                "price",
            "delete_item_from_cart"]



class OrderItemDetailSerializer(serializers.ModelSerializer):
    product         =   ProductDetailSerializer()
    class Meta:
        model      = OrderItem
        fields     = ["product"]

class CartDetailforOrderSerializer(WritableNestedModelSerializer):
    # product         =   OrderItemDetailSerializer()
    class Meta:
        model      = Cart
        fields     = "__all__"
