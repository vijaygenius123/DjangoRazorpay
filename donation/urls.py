from django.urls import path
from .views import home, success

urlpatterns = [
    path('',home),
    path('success/', success, name='success')
]