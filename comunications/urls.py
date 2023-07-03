from django.contrib import admin
from django.urls import path, include
from comunications.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('comunications/', comunications, name="comunications"),
    path("comunications_form/", comunications_form, name="comunications_form"),
    path("comunications_search/", comunications_search, name="comunications_search"),
    path("comunications_delete/<int:pk>", DeleteComunication.as_view(), name="comunications_delete"),
]