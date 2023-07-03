from django.contrib import admin
from django.urls import path, include
from main.views import *
from django.conf.urls.static import static
from django.conf import settings

handler404 = 'main.views.error_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),

    path("index/", index, name="index"),
    path("about/", about, name="about"),

    # path('', login_request, name="Login"),
    # path('login', login_request, name="Login"),
    # path('register', register, name='Register'),

    path('', include('accounts.urls')),
    path('', include('courses.urls')),
    path('', include('students.urls')),
    path('', include('professors.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)