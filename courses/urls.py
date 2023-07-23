from django.contrib import admin
from django.urls import path, include
from courses.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("courses/", courses, name="courses"),
    path("courses/<id>", courses, name="courses"),
    path("courses-delete/<int:pk>", CourseDelete.as_view(), name="courses_delete"),
    path("courses-form/", courses_form, name="courses_form"),
    path("courses-search/", courses_search, name="courses_search"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)