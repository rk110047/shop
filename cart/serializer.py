from rest_framework import serializers
from product.serializer import ProductDetailForCartSerializer
from .models import Cart
from .models import OrderItem
from product.serializer import ProductDetailSerializer


class CartDetailSerializer(serializers.ModelSerializer):
    # remove_from_cart     =    serializers.HyperlinkedIdentityField(view_name='cart:remove_from_cart',lookup_field='product_id')
    delete_item_from_cart = serializers.HyperlinkedIdentityField(view_name='cart:delete_item_from_cart',lookup_field='item_id')
    # url             =   serializers.HyperlinkedIdentityField(view_name='product:detail product',lookup_field='product_id')
    # product         =   ProductDetailForCartSerializer(read_only=True)
    # item              =   serializers.SerializerMethodField()
    class Meta:
        model      = OrderItem
        fields     = ["product",
                  "quantity",
                "price",
            "delete_item_from_cart"]


class OrderItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model      = OrderItem
        fields     = "__all__"
