from django.urls import path
from topics.views import TopicListCreateAPIView


urlpatterns = [
    path("", TopicListCreateAPIView.as_view(), name="topics"),
]
