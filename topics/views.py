from rest_framework.generics import ListCreateAPIView
from .models import Topic, Vote
from .serializers import TopicSerializer


class TopicListCreateAPIView(ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
