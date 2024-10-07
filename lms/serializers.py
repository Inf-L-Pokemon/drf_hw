from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import YoutubeLinksValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YoutubeLinksValidator(field='links_to_video')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    @staticmethod
    def get_lessons_count(obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = '__all__'
