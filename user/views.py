from django.contrib.auth.models import make_password
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer


class UserLogin(APIView):

    def post(self, req):
        username = req.data.get('username')
        password = req.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'token': str(refresh.access_token)
            }, status=200)

        return JsonResponse({
            'message': 'User not found'
        }, status=401)


class UserCreate(APIView):

    def post(self, req):
        data = req.data
        user = User.objects.filter(username=data['username']).first()

        if user is not None:
            return JsonResponse({
                'error': 'username already exists'
            }, status=400)

        new_user = User.objects.create(**data)
        new_user.password = make_password(data['password'])
        new_user.save()
        serializer = UserSerializer(new_user)
        return JsonResponse(serializer.data, safe=True, status=201)
