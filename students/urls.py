from django.contrib import admin
from django.urls import path, include
from students.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("students/", students, name="students"),
    path("students/<id>", students, name="students"),
    path("students_form/", students_form, name="students_form"),
    path("students_search/", students_search, name="students_search"),
    path("students_delete/<int:pk>", DeleteStudent.as_view(), name="students_delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)