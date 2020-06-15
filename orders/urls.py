from django.urls import path
from .views import OrdersAPIView,PlaceOrder



urlpatterns =[
	path("",OrdersAPIView.as_view(),name='orders'),
	path("place/",PlaceOrder.as_view(),name="place order")

]