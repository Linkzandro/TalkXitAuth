from rest_framework import serializers
from ..models import UserProfile
from django.contrib.auth.password_validation import validate_password

class UserProfileCreateSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2=serializers.CharField(write_only=True,required=True)
    class Meta:
        model=UserProfile
        fields = ['name', 'email', 'password','password2','birthday']
    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError('senhas não coincidem')
        return attrs