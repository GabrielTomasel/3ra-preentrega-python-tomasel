from django.contrib import admin
from django.urls import path
from preentrega3.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="Index"),
    path("students/", students, name="Students"),
    path("students_form/", students_form, name="Students Form"),
    path("students_search/", students_search, name="Students Search"),
    path("courses/", courses, name="Courses"),
    path("courses_form/", courses_form, name="Courses Form"),
    path("courses_search/", courses_search, name="Courses Search"),
    path("professors_form/", professors_form, name="Professors Form"),
    path("professors_search/", professors_search, name="Professors Search"),
]
