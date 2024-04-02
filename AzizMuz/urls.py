from django.contrib import admin
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.urls import path, include

handler404 = 'main.views.custom_404'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)