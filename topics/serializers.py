from rest_framework import serializers
from topics.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(read_only=True)
    dislikes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Topic
        fields = ("title", "description", "likes", "dislikes")
