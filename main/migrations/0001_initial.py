# Generated by Django 4.2.1 on 2024-01-10 17:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('comment', models.TextField(max_length=2048)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('compressed_image', models.ImageField(blank=True, upload_to='images')),
                ('title', models.CharField(max_length=512)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('music', models.FileField(upload_to='musics/', validators=[django.core.validators.FileExtensionValidator(['mp3', 'wav', 'ogg', 'm4a', 'wma'])])),
                ('music_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Music',
            },
        ),
        migrations.CreateModel(
            name='SubscribeEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('upcoming_date', models.DateField()),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'Event',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000, verbose_name='YouTube linkni kiriting')),
                ('song_type', models.CharField(choices=[('single', 'Single'), ('duet', 'Duet'), ('trio', 'Trio'), ('quartet', 'Quartet')], default='single', max_length=16, verbose_name="Qo'shiq turi")),
                ('title', models.CharField(max_length=128, verbose_name='Video sarlavhasi')),
                ('desc', models.TextField(blank=True, max_length=128, null=True, verbose_name="Qo'shimcha tavsif")),
                ('thumb', models.ImageField(blank=True, upload_to='images/', verbose_name='Video muqova rasmi')),
                ('add_time', models.DateField(auto_now_add=True)),
                ('dur', models.CharField(blank=True, max_length=255, verbose_name="Video davomiyligi (misol:'23:14')")),
            ],
            options={
                'db_table': 'Video',
            },
        ),
        migrations.CreateModel(
            name='VisitorCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'VisitorCounter',
            },
        ),
    ]
