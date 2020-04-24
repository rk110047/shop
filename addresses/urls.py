from django.urls import path
from .views import ShippingAddressCreateAPIView,BillingAddressCreateAPIView

urlpatterns=[
    path('shipping/',ShippingAddressCreateAPIView.as_view(),name="shipping address create"),
    path('billing/',BillingAddressCreateAPIView.as_view(),name="billing address create")

]
