from rest_framework.generics import  CreateAPIView
from .serializers import UserProfileCreateSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

class CreateUserProfile(CreateAPIView):
    serializer_class=UserProfileCreateSerializer
    permission_classes=[AllowAny]

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile=serializer.save()
        refresh=RefreshToken.for_user(profile)
        
        return Response({
            'access':str(refresh.access_token),
            'refresh':str(refresh),
        },status=status.HTTP_201_CREATED)