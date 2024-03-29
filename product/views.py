from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from .models import Product,Categories
from django.db.models import Q
from .serializer import ProductSerializer,ProductDetailSerializer,ProductCreateSerializer,ProductListOfUserSerializer,ProductDetailForListSerializer,ProductUpdateSerializer,CreateCatSerializer
from django.contrib.auth.decorators import login_required
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductDetailSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'product_id'

class ProductDetailForScannerAPIView(generics.RetrieveAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductDetailSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'product_code'



class ProductListAPIView(generics.ListAPIView):
    # queryset                =   Product.objects.all()
    serializer_class        =   ProductSerializer
    permission_classes      =   []
    authentication_classes  =   []



    def get_queryset(self):
        request    =    self.request
        print(request.user)
        queryset   =    Product.objects.filter(active=True)
        print(queryset)
        return queryset


class ProductSearchAPIView(generics.ListAPIView):
    # queryset                =   Product.objects.all()
    serializer_class        =   ProductSerializer
    permission_classes      =   []
    authentication_classes  =   []



    def get_queryset(self):
        request    =    self.request
        queryset   =    Product.objects.all()
        query      =    request.GET.get('q')
        if query is not None:
            queryset     =    queryset.filter(Q(product_name__icontains=query))
                                                # Q(brand_name__icontains=query))
                                                # Q(shop__icontains=query))

        return queryset



class ProductCreateAPIView(generics.CreateAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductCreateSerializer
    permission_classes      =   []
    authentication_classes  =   [JSONWebTokenAuthentication,SessionAuthentication]

    # @login_required
    def post(self,request,*args,**kwargs):
        try:
            self.create(request,*args,**kwargs)
            return Response({"status":201})
        except:
            return Response({"message":"form invaild and price,quantity are integer field"})

    def perform_create(self,serializer):
        shop_name       =   self.request.user.shopprofile
        serializer.save(user=self.request.user,shop_name=shop_name)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductCreateSerializer
    permission_classes      =   [IsOwnerOrReadOnly]
    authentication_classes  =   [SessionAuthentication]
    lookup_field            =   'product_id'


class GetProductById(generics.ListAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'user'
    
    def get(self,request,user,*args,**kwargs):
        queryset     =    Product.objects.filter(user=user) 
        serializer   =    ProductSerializer(queryset,many=True,context={'request': request})       
        return Response(serializer.data)
    

class ProductListOfUserAPIView(generics.ListAPIView):
    # queryset                =   Product.objects.all()
    serializer_class        =   ProductListOfUserSerializer
    permission_classes      =   []
    authentication_classes  =   [JSONWebTokenAuthentication,SessionAuthentication]



    def get_queryset(self):
        request    =    self.request
        user       =    request.user
        queryset   =    Product.objects.filter(user=user)
        query      =    request.GET.get('q')
        if query is not None:
            queryset     =    queryset.filter(Q(product_name__icontains=query))
                                                # Q(brand_name__icontains=query))
                                                # Q(shop__icontains=query))

        return queryset



class ProductDetailOfListAPIView(generics.RetrieveAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductDetailForListSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'product_id'


class ProductEditAPIView(generics.UpdateAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductUpdateSerializer
    permission_classes      =   []
    authentication_classes  =   [JSONWebTokenAuthentication,SessionAuthentication]
    lookup_field            =   'product_id'


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductUpdateSerializer
    permission_classes      =   []
    authentication_classes  =   [JSONWebTokenAuthentication,SessionAuthentication]
    lookup_field            =   'product_id'


class CategoriesAPIView(generics.CreateAPIView):
    queryset                =   Categories.objects.all()
    serializer_class        =   CreateCatSerializer
    permission_classes      =   []
    authentication_classes  =   []

    