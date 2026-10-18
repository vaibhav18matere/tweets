
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet_poster/', include('tweet_poster.urls')),
    path('', lambda request: redirect('index')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
