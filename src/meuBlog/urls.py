from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import index
from .views import post
from .views import about
from .views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('posts/<int:post_id>', post),
    path('about/', about),
    path('contact/', contact),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)