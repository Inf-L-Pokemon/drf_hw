from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from lms.models import Course
from users.models import User


@shared_task
def send_mail_update_course(course_id):
    """Отправляет сообщение об обновлении курса на почту пользователям, которые подписаны на этот курс."""

    course = Course.objects.get(pk=course_id)
    send_mail(
        subject=f'Обновление курса "{course.title}"!',
        message=f'Курс "{course.title}" был обновлен. Зайдите на страницу курса, чтобы узнать подробности.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscription.user.email for subscription in course.subscriptions.all()],
        fail_silently=False
    )


@shared_task
def check_last_login():
    """Делает не активным пользователя, который заходил последний раз более 30 дней назад"""

    users = User.objects.filter(is_active=True)
    for user in users:
        if timezone.now() - user.last_login > timezone.timedelta(days=30):
            user.is_active = False
            user.save()
