from rest_framework.generics import  CreateAPIView,ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import UserProfileCreateSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import UserProfile


class ProfileAPIView(ModelViewSet):
    serializer_class=UserProfileCreateSerializer
    queryset=UserProfile.objects.all()
    http_method_names=['get','post','patch']
    
    def get_object(self):
        return self.request.user
    def get_permissions(self):
        if self.action=='create':
            return [AllowAny()]
        return super().get_permissions()
    
    def list(self, request, *args, **kwargs):
        return self.retrieve(request)
