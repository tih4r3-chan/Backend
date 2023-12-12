from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserProfileSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        response_data = serializer.data

        # response_data['message'] = 'Registro exitoso'
        # response_data['redirect_url'] = 'http://127.0.0.1:3000/frontend/login/'

        headers = self.get_success_headers(response_data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
