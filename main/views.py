from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import *


class Index(View):
    email_field = SubscribeNews

    def get(self, req):
        latest_music = Videos.objects.latest('id')

        musics_list = Musics.objects.order_by('-id')[:5]
        musics = list(enumerate(musics_list))
        mus_list = []
        for i, j in musics:
            i += 1
            mus_list.append((i, j))

        videos_list = Videos.objects.order_by('-id')[1:4]
        return_context = {"latest_music": latest_music, "emailfield": self.email_field, "musics": mus_list,
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
        musics = list(enumerate(musics_list))
        mus_list = []
        for i, j in musics:
            i += 1
            print(j.music)
            mus_list.append((i, j))

        return render(req, 'main/02.html',{'musics':mus_list})


class VideosView(View):
    def get(self, req):
        return render(req, 'main/videos.html')
