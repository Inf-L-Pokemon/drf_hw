from rest_framework import serializers

from lms.models import Course, Lesson, Subscription
from lms.validators import YoutubeLinksValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YoutubeLinksValidator(field='links_to_video')]


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    @staticmethod
    def get_lessons_count(obj):
        return obj.lessons.count()

    def get_subscription(self, obj):
        user = self.context['request'].user
        return obj.subscriptions.filter(user=user).exists()

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
