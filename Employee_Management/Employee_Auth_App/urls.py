from django.urls import path
from .views import ( SignUp , SignIn , SignOut )

urlpatterns = [
    path('signup/',SignUp.as_view(),name='SignUp'),
    path('signin/',SignIn.as_view(),name='SignIn'),
    path('signout/',SignOut.as_view(),name='SignOut'),
]