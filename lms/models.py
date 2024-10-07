from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', help_text='Название курса')
    preview = models.ImageField(upload_to='lms/course/preview', verbose_name='Превью', help_text='Загрузите превью',
                                **NULLABLE)
    description = models.TextField(verbose_name='Описание', help_text='Описание курса', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', help_text='Название урока')
    preview = models.ImageField(upload_to='lms/lesson/preview', verbose_name='Превью', help_text='Загрузите превью',
                                **NULLABLE)
    description = models.TextField(verbose_name='Описание', help_text='Описание урока', **NULLABLE)
    links_to_video = models.URLField(verbose_name='Ссылка на видео', help_text='Ссылка на видео по уроку', **NULLABLE)

    courses = models.ManyToManyField(Course, related_name='lessons', verbose_name='Курсы')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
