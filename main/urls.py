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
    path('videos-api/data/<str:code>', SendVideoData.as_view(), name='videos_data_locate'),
    path('videos-api/data/', VideosJsonView.as_view(), name='videos_data'),
    path('blog/images/blog/<str:image_name>', image_download_blog, name='image_download_blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog'),
    path('blog/', PostBlogView.as_view(), name='blogs'),
    path('imgs-api/data/<int:number>', get_picture_links, name='get_picture_links'),
    path('imgs-api/cnt/', get_picture_links_count, name='get_picture_links_count'),
    path('subscribe-email/', subscribe_email, name='subscribe-email'),
]
