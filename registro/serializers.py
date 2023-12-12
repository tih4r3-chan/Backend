from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

    def validate(self, data):
        # Validar que las contraseñas coincidan
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Las contraseñas no coinciden.")

        # Validar la complejidad de la contraseña
        validate_password(data['password'])

        return data

    def create(self, validated_data):
        del validated_data['password_confirmation']

        user = User.objects.create_user(**validated_data)
        return user
