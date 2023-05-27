from django.shortcuts import render, redirect
from django.views import View
from .forms import *


class Index(View):
    email_field = SubscribeNews

    def get(self, req):
        return render(req, 'main/index.html', context={"latest_music": None, "emailfield": self.email_field})

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
        return render(req, 'main/musics.html')


class VideosView(View):
    def get(self, req):
        return render(req, 'main/videos.html')
