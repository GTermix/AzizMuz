import shutil
import os
from django.contrib import admin
from .models import *

admin.site.register(Videos)
admin.site.register(Musics)
admin.site.register(Images)
admin.site.register(UpcomingEvents)
