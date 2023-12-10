from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError
class Registerserializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'repeat_password')


