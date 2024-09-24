from django.urls import path

from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/list/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/<int:pk>/delete', LessonDestroyAPIView.as_view(), name='lesson-delete'),
] + router.urls
