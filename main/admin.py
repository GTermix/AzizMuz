import shutil
import os
from django.contrib import admin
from .models import *

admin.site.register(Videos)
admin.site.register(Musics)


class ImagesClass(admin.ModelAdmin):
    exclude = ('compressed_image',)


admin.site.register(Images, ImagesClass)
admin.site.register(UpcomingEvents)
