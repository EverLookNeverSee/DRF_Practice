from rest_framework import serializers
from topics.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ("title", "description", "likes", "dislikes")
        read_only_fields = ["likes", "dislikes"]
