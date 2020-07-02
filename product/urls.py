from django.urls import path
from .views import ProductCreateAPIView,ProductListAPIView,ProductSearchAPIView,ProductUpdateAPIView,ProductDetailAPIView,GetProductById,ProductDetailForScannerAPIView,ProductListOfUserAPIView,ProductDetailOfListAPIView,ProductEditAPIView,ProductDeleteAPIView,CategoriesAPIView


app_name='product'

urlpatterns=[
    path('',ProductListAPIView.as_view(),name='products'),
    path('create/',ProductCreateAPIView.as_view(),name='create product'),
    path('search/',ProductSearchAPIView.as_view(),name='search product'),
    path('listofuser/',ProductListOfUserAPIView.as_view(),name='user products list'),
    path('update/<product_id>',ProductUpdateAPIView.as_view(),name='update product'),
    path('detail/<product_id>',ProductDetailAPIView.as_view(),name='detail product'),
    path('detailoflist/<product_id>',ProductDetailOfListAPIView.as_view(),name='detail of product'),
    path('edit/<product_id>',ProductEditAPIView.as_view(),name='edit product'),
    path('delete/<product_id>',ProductDeleteAPIView.as_view(),name='delete product'),
    path('scan/<product_code>',ProductDetailForScannerAPIView.as_view(),name='scan and get'),
    path('shop_product/<user>',GetProductById.as_view(),name="shops product"),
    path('create/cat/',CategoriesAPIView.as_view(),name="create cat")




]
