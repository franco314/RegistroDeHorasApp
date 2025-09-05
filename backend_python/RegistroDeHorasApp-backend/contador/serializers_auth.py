from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        # Usamos create_user para que la contraseña se guarde encriptada
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
