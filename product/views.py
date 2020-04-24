from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from .models import Product
from django.db.models import Q
from .serializer import ProductSerializer,ProductDetailSerializer
from django.contrib.auth.decorators import login_required
from utils.permissions import IsOwnerOrReadOnly

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductDetailSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'product_id'



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
        print(query)
        if query is not None:
            queryset     =    queryset.filter(Q(product_name__icontains=query)|
                                                Q(brand_name__icontains=query))
                                                # Q(shop__icontains=query))

        return queryset



class ProductCreateAPIView(generics.CreateAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductSerializer
    # permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]

    # @login_required
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self,serializer):
        shop_name       =   self.request.user.shopprofile
        serializer.save(user=self.request.user,shop_name=shop_name)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductSerializer
    permission_classes      =   [IsOwnerOrReadOnly]
    authentication_classes  =   [SessionAuthentication]
    lookup_field            =   'product_id'
