from django.urls import path
from .views import DeliveryPersonProfileAPIView


urlpatterns =[
	path('profile/',DeliveryPersonProfileAPIView.as_view(),name='delivery person profile')
]