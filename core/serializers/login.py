from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data.get("email"),
            password=data.get("password")
        )

        if not user:
            raise serializers.ValidationError("Credenciais inválidas")

        data["user"] = user
        return data