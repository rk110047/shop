from django.urls import path
from .views import ShippingAddressCreateAPIView,BillingAddressCreateAPIView
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('shipping/',csrf_exempt(ShippingAddressCreateAPIView.as_view()),name="shipping address create"),
    path('billing/',csrf_exempt(BillingAddressCreateAPIView.as_view()),name="billing address create")

]
