from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='myprofile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.MEDIA_URL)
