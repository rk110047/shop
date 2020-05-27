from django.urls import path
from .views import ShopProfileCreateAPIView,ShopsAPIView


urlpatterns=[
    path('create-shop-profile/',ShopProfileCreateAPIView.as_view(),name='shop profile'),
    path('',ShopsAPIView.as_view(),name='shops')
]
