from django.db import models
from django.utils.translation import gettext_lazy as _


class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("topics")


class Vote(models.Model):
    class VoteChoice(models.TextChoices):
        like = "l", _("like")
        dislike = "d", _("dislike")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="votes")
    vote = models.CharField(max_length=12, choices=VoteChoice.choices)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Vote")
        verbose_name_plural = _("Votes")
