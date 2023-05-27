from django.db import models


class Musics(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256, null=True, blank=True)
    music = models.FileField(upload_to='musics/', null=True)
    music_photo = models.ImageField(upload_to='images/', null=True)
    upload_date = models.DateTimeField(auto_now_add=True)


class Videos(models.Model):
    title = models.CharField(max_length=128)
    caption = models.CharField(max_length=2048, null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True)
    thumb = models.ImageField(upload_to='images/', null=True)
    upload_date = models.DateTimeField(auto_now_add=True)


class Images(models.Model):
    image = models.ImageField(upload_to='images/', null=True)


class UpcomingEvents(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    upcoming_date = models.DateField()
    title = models.CharField(max_length=128)


class SubscribeEmail(models.Model):
    email = models.EmailField()
