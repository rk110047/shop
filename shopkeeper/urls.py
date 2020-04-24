from django.urls import path
from .views import ShopProfileCreateAPIView


urlpatterns=[
    path('create-shop-profile/',ShopProfileCreateAPIView.as_view(),name='shop profile'),
]
