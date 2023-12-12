from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .serializers import LoginSerializer

class UserLoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Autenticar al usuario
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response(
                {'error': 'Credenciales inválidas'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Generar o recuperar el token de autenticación
        token, created = Token.objects.get_or_create(user=user)

        # Puedes personalizar la respuesta según tus necesidades
        response_data = {
            'token': token.key,
            'username': user.username,
            'message': 'Inicio de sesión exitoso',
            # 'redirect_url': 'http://127.0.0.1:3000/login/',
        }

        headers = self.get_success_headers(response_data)
        return Response(response_data, status=status.HTTP_200_OK, headers=headers)
