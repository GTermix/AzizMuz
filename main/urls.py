from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('musics/', MusicsView.as_view(), name='musics'),
    path('videos/', VideosView.as_view(), name='videos')
]
