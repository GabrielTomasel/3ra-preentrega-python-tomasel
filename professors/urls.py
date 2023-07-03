from django.contrib import admin
from django.urls import path, include
from professors.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("professors/", professors, name="professors"),
    path("professors/<id>", professors, name="professors"),
    path("professors_form/", professors_form, name="professors_form"),
    path("professors_search/", professors_search, name="professors_search"),
    path("professors_delete/<int:pk>", DeleteProfessor.as_view(), name="professors_delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)