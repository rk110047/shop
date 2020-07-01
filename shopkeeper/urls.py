from django.urls import path
from .views import ShopProfileCreateAPIView,ShopsAPIView,ShopProfileDetailAPIView,ShopProfileEditAPIView


app_name="shop"

urlpatterns=[
    path('create-shop-profile/',ShopProfileCreateAPIView.as_view(),name='shop profile'),
    path('detail/',ShopProfileDetailAPIView.as_view(),name='shop detail'),
    path('edit/<id>',ShopProfileEditAPIView.as_view(),name='shop edit'),
    path('',ShopsAPIView.as_view(),name='shops')
]
