from rest_framework import generics,mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from .models import Cart,OrderItem
from .serializer import CartDetailSerializer,OrderItemDetailSerializer,CartDetailforOrderSerializer
from product.models import Product
from django.shortcuts import redirect
from django.core import serializers
from orders.models import  Order
from billing.models import BillingProfile
from addresses.models import Address
from django.views import View
import json




class ItemCreateAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       CartDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [SessionAuthentication]

    def get(self,request,product_id=None):
        request             =   self.request
        user                =   self.request.user
        if user.is_authenticated:
            orderitem            =  OrderItem.objects.filter(User=user)
            if orderitem.count()==0:
                product             =   Product.objects.get(product_id=product_id)
                item                =   OrderItem.objects.create()
                item.User.add(user)
                item.product = product
                item.price          =   product.product_price
                item.save()
                response    =   {"message":'item added succesfully'}
                return Response(response)
            else:
                try:
                    product             =   Product.objects.get(product_id=product_id)
                    item                =   OrderItem.objects.get(User=user,product=product,active=True)
                    item.quantity       +=1
                    item.save()
                    item.price           =   item.quantity*product.product_price
                    item.save()
                    response    =   {"message":'cart updated'}
                    return Response(response)
                except:
                    product             =   Product.objects.get(product_id=product_id)
                    item                =   OrderItem.objects.create()
                    item.User.add(user)
                    item.product=product
                    item.price          =   product.product_price
                    item.save()
                    response    =   {"message":'item added succesfully'}
                    return Response(response)
        return redirect("/auth/login/")

class RemoveItemFromCartAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       CartDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [SessionAuthentication]

    def get(self,request,product_id=None):
        request             =        self.request
        user                =        request.user
        if user.is_authenticated:
            try:
                product     =         Product.objects.get(product_id=product_id)
                item        =         OrderItem.objects.get(User=user,product=product)
                print(item.quantity)
                if item.quantity==1:
                    item.delete()
                    response        =   {"message":"item removed"}
                item.quantity -=1
                item.save()
                item.price           =   item.quantity*product.product_price
                item.save()
                response        =   {"message":"item updated"}
                return Response(response)
            except:
                response        =   {"message":"item is not in cart"}
                return Response(response)

        return redirect("/auth/login/")




class CartAPIView(generics.ListAPIView):
    # queryset                =       OrderItem.objects.all()
    serializer_class        =       CartDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [SessionAuthentication]

    def get_queryset(self):
        request             =   self.request
        user                =   self.request.user
        if user.is_authenticated:
            cart=OrderItem.objects.filter(User=user,active=True)
            # cart  =  Cart.objects.get(User=user)
            # cart  = cart.product.all()
            # print(cart)
            # if cart:
            #     qs = cart.product.all()
            #     print(qs)
            return cart

    def get(self,request):
        request             =   self.request
        user                =   self.request.user
        if user.is_authenticated:

            try:
                cart        =  Cart.objects.filter(User=user)
                object = Cart.objects.filter(User=user,active=True)
                for x in object:
                    object=x
                if OrderItem.objects.filter(User=user,active=True):
                    qs = OrderItem.objects.filter(User=user,active=True)
                    for x in qs:
                        object.product.add(x)
                total = 0
                for x in object.product.all():
                    total    +=  x.price
                object.total_price  = total
                total = 0
                for x in object.product.all():
                    total    +=  x.quantity
                object.total_items  = total
                object.save()
                # qs = Cart.objects.get(User=user)
                # qs = Cart.objects.get(id=qs.id)
                # product = []
                # for x in object.product.all():
                #     products = x.product
                #     product.append({"product name":products.product_name,
                #                     "product price":products.product_price})
                queryset = self.get_queryset()
                serializer = CartDetailSerializer(queryset, many=True,context={'request': request})
                print(serializer.data)
                response        ={"products":serializer.data,'total_items':object.total_items,'cart_total':object.total_price,}
                return Response(response)
                # response        ={'data':{"products":product,'total items':qs.total_items,'cart total':qs.total_price,}}
                # return Response(response)

            except:
                object =  Cart.objects.create()
                object.User.add(user)
                object.save()
                if OrderItem.objects.filter(User=user,active=True):
                    qs = OrderItem.objects.filter(User=user,active=True)
                    for x in qs:
                        object.product.add(x)
                total = 0
                for x in object.product.all():
                    total    +=  x.price
                object.total_price  = total
                total = 0
                for x in object.product.all():
                    total    +=  x.quantity
                object.total_items  = total
                object.save()
                queryset = self.get_queryset()
                serializer = CartDetailSerializer(queryset, many=True,context={'request': request})
                print(serializer.data)
                response        ={"products":serializer.data,'total_items':object.total_items,'cart_total':object.total_price,}
                return Response(response)


        else:
            response        =   {"message":"create session login..."}
            return Response(response)

class CheckOutAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       []
    permission_classes      =       []
    authentication_classes  =       [SessionAuthentication]

    def get(self,request):
        request             =   self.request
        user                =   self.request.user
        if user.is_authenticated:
            try:
                cart_obj        =   Cart.objects.filter(User=user,active=True)
                cart_obj        =   cart_obj.first()
                order_obj       =   Order.objects.filter(cart=cart_obj,active=True,ordered=False)
                order_obj       =   order_obj.first()
                order_obj.total =   cart_obj.total_price
                order_obj.save()
                response        =    {"order id":order_obj.order_id,"cart total":cart_obj.total_price,"shipping_total":order_obj.shipping_total,"order totel":order_obj.total}
                return Response(response)
            except:
                cart_obj                 =   Cart.objects.filter(User=user,active=True)
                cart_obj                 =   cart_obj.first()
                billing_profile,created  =   BillingProfile.objects.get_or_create(User=user,email=user.email)
                shipping_address         =   Address.objects.get(billingprofile=billing_profile,address_type="SHIPPING")
                shipping_address         =   shipping_address.last()
                billing_address          =   Address.objects.get(billingprofile=billing_profile,address_type="BIILING")
                billing_address          =   billing_address.last()
                order_obj                =   Order.objects.create(cart=cart_obj,billing_profile=billing_profile,billing_address=billing_address,shipping_address=shipping_address)
                response                 =    {"order id":order_obj.order_id,"cart total":cart_obj.total_price,"shipping_total":order_obj.shipping_total,"order total":order_obj.total}
                return Response(response)



class OrderItemDeleteAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       OrderItemDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [SessionAuthentication]

    def get(self,request,item_id=None):
        request             =        self.request
        user                =        request.user
        if user.is_authenticated:
            try:
                item        =         OrderItem.objects.get(User=user,item_id=item_id)
                item.delete()
                response        =   {"message":"item removed"}
                return Response(response)
            except:
                response        =   {"message":"item is not in cart"}
                return Response(response)

        return redirect("/auth/login/")


class getCartAPIView(generics.RetrieveAPIView):
    queryset                =       Cart.objects.all()
    serializer_class        =       CartDetailforOrderSerializer
    permission_classes      =       []
    authentication_classes  =       [SessionAuthentication]
    lookup_field            =       "id"


class orderItemCartAPIView(generics.RetrieveAPIView):
    queryset                =       OrderItem.objects.all()
    serializer_class        =       OrderItemDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [SessionAuthentication]
    lookup_field            =       "item_id"





