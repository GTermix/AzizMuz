from django.db import models


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
    thumb = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Video'


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
