from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Введите вашу существующую почту')

    phone = models.CharField(max_length=13, verbose_name='Телефон', help_text='Ваш номер телефона', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', help_text='Название города в котором живете',
                            **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', help_text='Загрузите аватар',
                               **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
