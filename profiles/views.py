from django.shortcuts import render
from .serializers import GetUserNetSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework import permissions

class UserNetView(ModelViewSet):
    '''Вывод пользователей'''
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]