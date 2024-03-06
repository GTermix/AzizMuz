import shutil
import os
from django.contrib import admin
from django.forms.models import inlineformset_factory
from .models import *


class ImageForBlogClass(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
class VideoForBlogClass(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class ImagesClass(admin.ModelAdmin):
    exclude = ('compressed_image',)
class PostClass(admin.ModelAdmin):
    exclude = ('views', 'medias')

admin.site.register(Video)
admin.site.register(Music)
admin.site.register(ImageForBlog,ImageForBlogClass)
admin.site.register(VideoForBlog,VideoForBlogClass)
admin.site.register(Post,PostClass)
admin.site.register(Image, ImagesClass)
admin.site.register(UpcomingEvent)
