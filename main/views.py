from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from pytube import YouTube
from .models import *
from django.http import FileResponse
from .forms import *

'''from pytube import YouTube

yt = YouTube('[VIDEO_URL]')
duration = yt.length
'''


class Index(View):
    email_field = SubscribeNews

    def get(self, req):
        latest_music = Videos.objects.latest('id')

        musics_list = Musics.objects.order_by('-id')[:5]
        musics = list(enumerate(musics_list, start=1))
        videos_list = Videos.objects.order_by('-id')[1:4]
        return_context = {"latest_music": latest_music, "emailfield": self.email_field, "musics": musics,
                          "videos": videos_list}
        return render(req, 'main/index.html', context=return_context)

    def post(self, req):
        form = SubscribeNews(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        return


class About(View):
    def get(self, req):
        return render(req, 'main/about.html')

    def post(self, req):
        pass


class ContactView(View):
    def get(self, req):
        return render(req, 'main/contact.html')

    def post(self, req):
        pass


class MusicsView(View):
    def get(self, req):
        musics_list = Musics.objects.order_by('-id')
        musics = list(enumerate(musics_list, start=1))
        return render(req, 'main/musics.html', {'musics': musics})


class VideosView(View):
    def get(self, req):
        latest_video = Videos.objects.order_by('-id')[0]
        # latest_video.link = latest_video.link.split('=')[1]
        videos_list = Videos.objects.order_by('-id')[1:]
        return render(req, 'main/videos.html', {"latest": latest_video, 'list': videos_list})


class AlbumView(View):
    def get(self, req):
        album = Images.objects.order_by('-id')[:20]
        return render(req, 'album.html', {"album": album})


def get_picture_links(request):
    data = Images.objects.order_by('-id').values('image', 'title', 'date')[20:]
    formatted_data = []
    for item in data:
        date_object = item['date']
        formatted_date = date_object.strftime('%b. %d, %Y')
        formatted_item = {
            'image': item['image'],
            'title': item['title'],
            'date': formatted_date
        }
        formatted_data.append(formatted_item)
    return JsonResponse(formatted_data, safe=False)


def music_download(request, music_name):
    music = get_object_or_404(Musics, music="musics/" + music_name)
    music_path = music.music.path
    return FileResponse(open(music_path, 'rb'), as_attachment=True)


def image_download(request, image_name):
    image = get_object_or_404(Images, image="images/" + image_name)
    image_path = image.image.path
    return FileResponse(open(image_path, 'rb'), as_attachment=True)
