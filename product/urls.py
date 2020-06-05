from django.urls import path
from .views import ProductCreateAPIView,ProductListAPIView,ProductSearchAPIView,ProductUpdateAPIView,ProductDetailAPIView,GetProductById


app_name='product'

urlpatterns=[
    path('',ProductListAPIView.as_view(),name='products'),
    path('create/',ProductCreateAPIView.as_view(),name='create product'),
    path('search/',ProductSearchAPIView.as_view(),name='search product'),
    path('update/<product_id>',ProductUpdateAPIView.as_view(),name='update product'),
    path('detail/<product_id>',ProductDetailAPIView.as_view(),name='detail product'),
    path('shop_product/<User>',GetProductById.as_view(),name="shops product")




]
