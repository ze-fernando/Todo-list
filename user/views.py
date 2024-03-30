from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserLogin(APIView):

    def post(self, req):
        username = req.data.get('user')
        password = req.data.get('pass')

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
        ...
