from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class UserLogin(APIView):

    def post(self, req):
        username = req.data.get('username')
        password = req.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'refresh': str(refresh)
            })

        return JsonResponse({
            'message': 'User not found'
        }, status=404)


class UserCreate(APIView):

    def post(self, req):
        data = req.data
        user = User.objects.filter(username=data['username']).first()

        if user is not None:
            return JsonResponse({
                'error': 'username already exists'
            }, status=400)

        new_user = User.objects.create(**data)  # nao salva senha haseada
        new_user.save()
        return JsonResponse({
            'message': 'user created successfully'  # temporario
        })
