from rest_framework.generics import ListCreateAPIView, CreateAPIView
from .models import Topic, Vote
from .serializers import TopicSerializer, VoteSerializer


class TopicListCreateAPIView(ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class VoteCreateAPIView(CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
