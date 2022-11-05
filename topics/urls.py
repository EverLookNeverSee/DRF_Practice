from django.urls import path
from topics.views import TopicListCreateAPIView, VoteCreateAPIView


urlpatterns = [
    path("", TopicListCreateAPIView.as_view(), name="topics"),
    path("votes/", VoteCreateAPIView.as_view(), name="vote-create")
]
