from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from pytube import YouTube


class Musics(models.Model):
    title = models.CharField(max_length=128)
    music = models.FileField(upload_to='musics/')
    music_photo = models.ImageField(upload_to='images/', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Music"


class Videos(models.Model):
    CHOICES = (
        ('single', 'Single'),
        ('duet', 'Duet'),
        ('trio', 'Trio'),
        ('quartet', 'Quartet')
    )
    link = models.CharField(max_length=1000)
    song_type = models.CharField(max_length=16, choices=CHOICES, default='single')
    title = models.CharField(max_length=128)
    desc = models.TextField(max_length=128, null=True, blank=True)
    thumb = models.ImageField(upload_to='images/', null=True, blank=True)
    add_time = models.DateField(auto_now_add=True)
    dur = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     db_table = 'Video'


@receiver(post_save, sender=Videos)
def edit_admin(sender, instance, **kwargs):
    if instance.link:
        yt = YouTube(instance.link)
        instance.dur = str(yt.length // 60) + ":" + str(yt.length % 60)
        if not instance.thumb:
            instance.thumb = yt.thumbnail_url
        else:
            instance.thumb.name = 'media/' + instance.thumb.name
        if not instance.desc:
            instance.desc = yt.description
        # instance.save()
        Videos.objects.filter(pk=instance.pk).update(
            dur=instance.dur,
            thumb=instance.thumb,
            desc=instance.desc
        )


class Images(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return "Image"

    class Meta:
        db_table = "Image"


class UpcomingEvents(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    upcoming_date = models.DateField()
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Event"


class SubscribeEmail(models.Model):
    email = models.EmailField()
