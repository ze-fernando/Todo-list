from django.urls import path
from .views import UserLogin, UserCreate

urlpatterns = [
    path('login/', UserLogin.as_view()),
    path('register/', UserCreate.as_view())
]
