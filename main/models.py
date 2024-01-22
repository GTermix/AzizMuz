import os
import requests
from AzizMuz.settings import MEDIA_ROOT
from django.db import models
from django.db.models.signals import post_save
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.urls import reverse
from PIL import Image


class Music(models.Model):
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


class Video(models.Model):
    CHOICES = (
        ('single', 'Single'),
        ('duet', 'Duet'),
        ('trio', 'Trio'),
        ('quartet', 'Quartet')
    )
    link = models.CharField(max_length=1000, verbose_name="YouTube linkni kiriting")
    song_type = models.CharField(max_length=16, choices=CHOICES, default='single', verbose_name="Qo'shiq turi")
    title = models.CharField(max_length=128, verbose_name="Video sarlavhasi")
    desc = models.TextField(max_length=128, null=True, blank=True, verbose_name="Qo'shimcha tavsif")
    thumb = models.ImageField(upload_to='images/',blank=True, verbose_name="Video muqova rasmi")
    add_time = models.DateField(auto_now_add=True)
    dur = models.CharField(max_length=255,blank=True, verbose_name="Video davomiyligi (misol:'23:14')")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Video'


@receiver(post_save, sender=Video)
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


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    compressed_image = models.ImageField(upload_to='images', blank=True)
    title = models.CharField(max_length=512)
    date = models.DateField(auto_now_add=True, blank=True)  # upload to pcloud tests.py

    def __str__(self):
        return f"{self.title} - {self.date}"

    class Meta:
        db_table = "Image"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        album = Images.objects.order_by('-id').first()
        old_file_path = os.path.join(MEDIA_ROOT, f'{album.image}')
        new_file_path = os.path.join(MEDIA_ROOT, 'images', f'photo_{album.pk}.{str(album.image)[-3:]}')
        os.rename(old_file_path,
                  new_file_path)
        image = Image.open(new_file_path)
        width, height = image.size
        new_size = (width // 2, height // 2)
        resized_image = image.resize(new_size)
        new_file_pathc = os.path.join(MEDIA_ROOT, 'images', f'photoc_{album.pk}.{str(album.image)[-3:]}')
        resized_image.save(f'{new_file_pathc}', optimize=True, quality=1)
        original_size = os.path.getsize(new_file_path)
        compressed_size = os.path.getsize(new_file_pathc)
        Images.objects.filter(pk=album.pk).update(
            image=f'images/photo_{album.pk}.{str(album.image)[-3:]}',
            compressed_image=f"images/photoc_{album.pk}.{str(album.image)[-3:]}"
        )


class UpcomingEvent(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    upcoming_date = models.DateField()
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Event"


class SubscribeEmail(models.Model):
    email = models.EmailField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    comment = models.TextField(max_length=2048)
    date=models.DateField(auto_now_add=True)

class VisitorCounter(models.Model):
    count = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return "Visitors Count"

    class Meta:
        db_table = "VisitorCounter"
