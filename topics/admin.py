from django.contrib import admin

from topics.models import Topic, Vote

admin.site.register(Topic)
admin.site.register(Vote)
