from rest_framework import serializers
from ..models import UserProfile
from django.contrib.auth.password_validation import validate_password

class UserProfileCreateSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2=serializers.CharField(write_only=True,required=True)
    class Meta:
        model=UserProfile
        fields = ['id','username','name','surname','email', 'password','password2','birthday']
        read_only_fields=['id']
    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError('senhas não coincidem')
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')

        return UserProfile.objects.create_user(**validated_data)