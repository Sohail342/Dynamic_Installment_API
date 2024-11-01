from rest_framework import serializers
from account.models import User

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ['email', 'password']

