import os
from AzizMuz.settings import MEDIA_ROOT
from django.db import models
from django.db.models.signals import post_save
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.urls import reverse


class Musics(models.Model):
    title = models.CharField(max_length=256)
    music = models.FileField(upload_to='musics/',
                             validators=[FileExtensionValidator(['mp3', 'wav', 'ogg', 'm4a', 'wma'])])
    music_photo = models.ImageField(upload_to='images/', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def get_music_url(self):
        return reverse('music_download', args=[self.music])

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
    thumb = models.ImageField(upload_to='images/', blank=True)
    add_time = models.DateField(auto_now_add=True)
    dur = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Video'


@receiver(post_save, sender=Videos)
def edit_admin(sender, instance, **kwargs):
    if instance.link:
        link = instance.link
        # instance.dur = str(yt.length // 60) + ":" + str(yt.length % 60)
        if not instance.thumb:
            instance.thumb = 'https://drive.google.com/thumbnail?id=' + link.split('/')[-2]
        else:
            instance.thumb.name = 'media/' + instance.thumb.name
        # instance.save()
        Videos.objects.filter(pk=instance.pk).update(
            thumb=instance.thumb,
            desc=instance.desc
        )


class Images(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=512)
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.date}"

    class Meta:
        db_table = "Image"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        album = Images.objects.order_by('-id').first()
        print(album.image)
        old_file_path = os.path.join(MEDIA_ROOT, f'{album.image}')
        new_file_path = os.path.join(MEDIA_ROOT, 'images', f'photo_{album.pk}.{str(album.image)[-3:]}')
        os.rename(old_file_path,
                  new_file_path)
        Images.objects.filter(pk=album.pk).update(
            image=f'images/photo_{album.pk}.{str(album.image)[-3:]}'
        )


class UpcomingEvents(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    upcoming_date = models.DateField()
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Event"


class SubscribeEmail(models.Model):
    email = models.EmailField()
