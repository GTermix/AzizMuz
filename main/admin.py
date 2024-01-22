import shutil
import os
from django.contrib import admin
from .models import *

admin.site.register(Video)
admin.site.register(Music)


class ImagesClass(admin.ModelAdmin):
    exclude = ('compressed_image',)


admin.site.register(Image, ImagesClass)
admin.site.register(UpcomingEvent)
