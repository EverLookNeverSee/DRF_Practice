from rest_framework import serializers
from topics.models import Topic, Vote


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ("title", "description", "likes", "dislikes")
        read_only_fields = ["likes", "dislikes"]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("topic", "vote")
