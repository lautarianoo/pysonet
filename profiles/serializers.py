from rest_framework import serializers

from .models import UserNet

class GetUserNetSerializer(serializers.ModelSerializer):
    '''Вывод инфо об юзере'''
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        exclude = ('password', 'last_login', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', )

class GetUserNetPublicSerializer(serializers.ModelSerializer):
    '''Вывод публичной инфо об юзере'''
    class Meta:
        model = UserNet
        exclude = ('password', 'last_login', 'is_active', 'is_staff', 'is_superuser', 'email', 'groups', 'user_permissions', 'phone', )

class UserByFollowerSerializer(serializers.ModelSerializer):
    '''Сериализация для подписоты'''
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        fields = ('id', 'username', 'avatar', )