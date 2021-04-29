from django.contrib.auth.models import AbstractUser
from django.db import models

class UserNet(AbstractUser):
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )

    '''КАСТОМНАЯ МАДЕОЛКЬА ЮЗЕРА'''
    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField('Первый логин', null=True)
    phone = models.CharField('Телефон',max_length=14)
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    technology = models.ManyToManyField('Technology', related_name='users')

class Technology(models.Model):
    '''Technology model'''
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name