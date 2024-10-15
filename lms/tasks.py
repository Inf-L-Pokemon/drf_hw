from celery import shared_task
from django.core.mail import send_mail

from config import settings
from lms.models import Course


@shared_task
def send_mail_update_course(course_id):
    """Отправляет сообщение об обновлении курса на почту пользователям, которые подписаны на этот курс."""

    course = Course.objects.get(pk=course_id)
    send_mail(
        subject=f'Обновление курса {course.title}!',
        message=f'Курс "{course.title}" был обновлен. Зайдите на страницу курса, чтобы узнать подробности.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscription.user.email for subscription in course.subscriptions.all()],
        fail_silently=False
    )
