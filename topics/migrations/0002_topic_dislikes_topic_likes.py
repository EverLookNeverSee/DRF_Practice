# Generated by Django 4.1.3 on 2022-11-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
