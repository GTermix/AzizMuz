import shutil
import os
from django.contrib import admin
from django.forms.models import inlineformset_factory
from unfold.admin import ModelAdmin
from .models import *

@admin.register(Image)
class UserAdmin(ModelAdmin):
    exclude = ('compressed_image',)
@admin.register(ImageForBlog)
class UserAdmin(ModelAdmin):
    def get_model_perms(self, request):
        return {}
@admin.register(VideoForBlog)
class UserAdmin(ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(Video)
class UserAdmin(ModelAdmin):
    exclude = ('dur','thumb','code')
@admin.register(Post)
class UserAdmin(ModelAdmin):
    exclude = ('views', 'medias')

@admin.register(Music)
class UserAdmin(ModelAdmin):
    pass
@admin.register(Events)
class UserAdmin(ModelAdmin):
    pass