import os
import datetime
import requests
import uuid
from AzizMuz.settings import MEDIA_ROOT
from django.db import models
from django.db.models.signals import post_save,m2m_changed
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image as Img
from pytube import YouTube



class Music(models.Model):
    title = models.CharField(max_length=256)
    music = models.FileField(upload_to='musics/',
                             validators=[FileExtensionValidator(['mp3', 'wav', 'ogg', 'm4a', 'wma'])])
    # music_photo = models.ImageField(upload_to='images/', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

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
    thumb = models.TextField(blank=True, verbose_name="Video muqova rasmi")
    add_time = models.DateField(auto_now_add=True)
    dur = models.CharField(max_length=255,blank=True)
    code=models.CharField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Video'
    
    def save(self, *args, **kwargs):
        import  re
        if not len(self.link)==11:
            l=str(self.link)
            yt = YouTube(l)
            yt_pattern = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
            match = re.match(yt_pattern, self.link)
            if match is not None:
                self.link = match.group(4)
            else:
                pattern2 = r"(?:https?://)?(?:www\.)?youtu\.be/([^/?]+)"
                video_code_match = re.match(pattern2,self.link).group(1)
                self.video_link = video_code_match
            time_delta = datetime.timedelta(seconds=yt.length)
            p=str(time_delta)
            self.dur = p[2:] if p.startswith("0:") else p[3:] if p.startswith("00:") else p
            self.thumb = yt.thumbnail_url
            if not self.desc:
                self.desc = yt.description
        super().save(*args,**kwargs)
        pk=self.pk
        a=uuid.uuid4().hex
        n=Video.objects.filter(link=self.link)
        code_ = f"{a[:16]}{pk}{a[16:]}"
        f=Video.objects.filter(pk=pk)
        f.update(code=code_)
        


# @receiver(post_save, sender=Video)
# def edit_admin(sender, instance, **kwargs):
#     if instance.link:
#         yt = YouTube(instance.link)
#         instance.dur = str(yt.length // 60) + ":" + str(yt.length % 60)
#         if not instance.thumb:
#             instance.thumb = yt.thumbnail_url
#         else:
#             instance.thumb.name = 'media/' + instance.thumb.name
#         if not instance.desc:
#             instance.desc = yt.description
#         # instance.save()
#         Video.objects.filter(pk=instance.pk).update(
#             dur=instance.dur,
#             thumb=instance.thumb,
#             desc=instance.desc
#         )


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
        obj = Image.objects.order_by('-id').first()
        old_file_path = os.path.join(MEDIA_ROOT, f'{obj.image}')
        img__=str(obj.image)
        ext=img__[img__.find('.'):].lower()
        new_file_path = os.path.join(MEDIA_ROOT, 'images', f'photo_{obj.pk}{ext}')
        os.rename(old_file_path,new_file_path)
        image = Img.open(new_file_path)
        width, height = image.size
        new_size = (width // 2, height // 2)
        resized_image = image.resize(new_size)
        new_file_pathc = os.path.join(MEDIA_ROOT, 'images', f'photoc_{obj.pk}{ext}')
        resized_image.save(f'{new_file_pathc}', optimize=True, quality=1)
        Image.objects.filter(pk=obj.pk).update(image=f'images/photo_{obj.pk}{ext}',
                                               compressed_image=f"images/photoc_{obj.pk}{ext}")


class Events(models.Model):
    title=models.CharField(max_length=128)
    description=models.TextField()
    image=models.ImageField(upload_to="images/event/",blank=True,null=True)
    link=models.URLField(verbose_name="Event Link")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        get_latest_by = 'id'
        db_table = "Events"


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

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Email'

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    comment = models.TextField(max_length=2048)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.date}"

    class Meta:
        db_table = 'Contact'

class ImageForBlog(models.Model):
    image = models.ImageField(upload_to='images/blog/')
    def __str__(self):
        return f"ImageForBlog - {self.id}"

    class Meta:
        db_table = 'ImageForBlog'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        obj = ImageForBlog.objects.order_by('-id').first()
        os.path
        old_file_path = os.path.join(MEDIA_ROOT, *str(obj.image).split("/"))
        img__=str(obj.image)
        ext=img__[img__.find('.'):].lower()
        new_file_path = os.path.join(MEDIA_ROOT, 'images','blog', f'photo_{obj.pk}{ext}')
        os.rename(old_file_path,new_file_path)
        ImageForBlog.objects.filter(pk=obj.pk).update(image=f'images/blog/photo_{obj.pk}{ext}')

class VideoForBlog(models.Model):
    video_link=models.CharField(max_length=256)

    def save(self, *args, **kwargs):
        import re
        yt_pattern = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
        match = re.match(yt_pattern, self.video_link)
        if match is not None:
            self.video_link = match.group(4)
        else:
            pattern2 = r"(?:https?://)?(?:www\.)?youtu\.be/([^/?]+)"
            video_code_match = re.match(pattern2,self.video_link).group(1)
            self.video_link = video_code_match
        super().save(*args,**kwargs)

    def __str__(self):
        return f"VideoForBlog - {self.id}"

    class Meta:
        db_table = 'VideoForBlog'

class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    image = models.ManyToManyField(ImageForBlog,blank=True, related_name='image_for_blog')
    video = models.ManyToManyField(VideoForBlog,blank=True, related_name='video_for_blog')
    medias=models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} - {self.created_at}"

    class Meta:
        get_latest_by = 'id'
        db_table = 'Post'

    # function to increase views count
    @property
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

@receiver(m2m_changed, sender=Post.image.through)
@receiver(m2m_changed, sender=Post.video.through)
def update_medias(sender, instance, **kwargs):
    instance.medias = instance.image.count() + instance.video.count()
    instance.save()

class VisitorCounter(models.Model):
    count = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Visitors Count - {self.id}"

    class Meta:
        db_table = "VisitorCounter"
