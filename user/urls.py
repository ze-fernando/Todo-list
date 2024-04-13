from django.urls import path
from .views import UserLogin, UserCreate

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('register/', UserCreate.as_view(), name='register')
]
