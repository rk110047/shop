from rest_framework import serializers
from product.serializer import ProductDetailForCartSerializer
from .models import Cart
from .models import OrderItem
from dynamic_rest.fields.fields import DynamicRelationField
from dynamic_rest.serializers import DynamicModelSerializer
from product.serializer import ProductDetailSerializer
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CartDetailSerializer(WritableNestedModelSerializer):
    # remove_from_cart     =    serializers.HyperlinkedIdentityField(view_name='cart:remove_from_cart',lookup_field='product_id')
    delete_item_from_cart = serializers.HyperlinkedIdentityField(view_name='cart:delete_item_from_cart',lookup_field='item_id')
    # url             =   serializers.HyperlinkedIdentityField(view_name='product:detail product',lookup_field='product_id')
    product         =   ProductDetailForCartSerializer()
    # item              =   serializers.SerializerMethodField()
    class Meta:
        model      = OrderItem
        fields     = ["item_id",
                    "product",
                  "quantity",
                "price",
            "delete_item_from_cart"]



class OrderItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model      = OrderItem
        fields     = "__all__"
