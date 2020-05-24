from django.urls import path
from .views import RegisterAPIView,LoginAPIView,RegisteredBySuperUserAPIView

urlpatterns=[
    path('login/',LoginAPIView.as_view(),name='login'),
    path('register/',RegisterAPIView.as_view(),name='register'),
    path('special/register/',RegisteredBySuperUserAPIView.as_view())



]
