from django.db.models import Count, Q
from rest_framework.generics import ListCreateAPIView
from .models import Topic, Vote
from .serializers import TopicSerializer


class TopicListCreateAPIView(ListCreateAPIView):
    queryset = Topic.objects.all().annotate(
        likes=Count("votes", filter=Q(votes__vote=Vote.VoteChoice.like)),
        dislikes=Count("votes", filter=Q(votes__vote=Vote.VoteChoice.dislike))
    )
    serializer_class = TopicSerializer
