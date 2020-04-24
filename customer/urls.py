from django.urls import path
from .views import CreateProfileAPIView,EditProfileAPIView,CustomerListAPIView



urlpatterns=[
    path('create/',CreateProfileAPIView.as_view()),
    path('update/',EditProfileAPIView.as_view()),
    path('list/',CustomerListAPIView.as_view())


]
