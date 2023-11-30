from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('images/images/<str:image_name>', image_download, name='image_download'),
    path('images/', AlbumView.as_view(), name='images'),
    path('musics/musics/<str:music_name>/', music_download, name='music_download'),
    path('musics/', MusicsView.as_view(), name='musics'),
    path('videos/', VideosView.as_view(), name='videos'),
    path('img-api/data/all/', get_picture_links, name='get_picture_links'),
]
