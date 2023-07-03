from django.contrib import admin
from django.urls import path, include
from main.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("index/", index, name="index"),
    path("about/", about, name="about"),

    path('', include('accounts.urls')),
    path('', include('courses.urls')),
    path('', include('students.urls')),
    path('', include('professors.urls')),
    path('', include('comunications.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.error_404_view'