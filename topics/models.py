from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        ordering = ("-likes",)
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


@receiver(post_save, sender=Vote)
def update_votes(sender, instance, **kwargs):
    if instance.vote == Vote.VoteChoice.like:
        Topic.objects.filter(id=instance.topic.id).update(likes=F("likes") + 1)
    else:
        Topic.objects.filter(id=instance.topic.id).update(dislikes=F("dislikes") + 1)
