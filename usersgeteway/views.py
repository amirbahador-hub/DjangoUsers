# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializes import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
