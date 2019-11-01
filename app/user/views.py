from rest_framework import generics
from rest_framework.authtoken.views import  ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializer import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenview(ObtainAuthToken):
    """create a new auth token for user"""
    serializer_class = AuthTokenSerializer

