from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from lms.models import Course, Lesson

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


class Payment(models.Model):
    payment_method = (('cash', 'Наличные'), ('transfer_to_account', 'Перевод на счет'))

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', related_name='payments',
                             null=True)
    date = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Курс для оплаты',
                                    related_name='payments', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Урок для оплаты',
                                    related_name='payments', **NULLABLE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Сумма оплаты', **NULLABLE)
    method = models.CharField(max_length=30, choices=payment_method, verbose_name='Способ оплаты', **NULLABLE)
    session_id = models.CharField(max_length=255, verbose_name='ID сессии', **NULLABLE)
    link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', **NULLABLE)

    def __str__(self):
        return f'{self.method} {self.amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
