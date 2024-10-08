from rest_framework.serializers import ValidationError


class YoutubeLinksValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        youtube_links = 'youtube.com'
        val = dict(value).get(self.field)
        if val and youtube_links not in val:
            raise ValidationError(f'Поле "{self.field}" должно содержать ссылку только на Youtube.')
