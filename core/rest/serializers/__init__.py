from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["uuid", "name", "email", "password", "phone"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 4}}
