from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Check if the input is a valid phone number or email
        user = None
        identifier = attrs.get(self.username_field)

        try:
            if "@" in identifier:
                user = User.objects.get(email=identifier)
            elif identifier.isdigit():
                user = User.objects.get(phone_number=identifier)
        except User.DoesNotExist:
            pass

        if user:
            data[self.username_field] = user.username

        return data
