from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import * 
from django.db.models import Q
from django.shortcuts import render
from .forms import *


def error_404_view(request, exception):
    template = loader.get_template('error404.html')
    context = {
        'error_url': request.path,
    }
    documment = template.render(context, request)
    return HttpResponse(documment)

# /////////////////////////////////////////////////////////////////

def index(request):
    template = loader.get_template('home.html')
    context = {
        'error_url': request.path,
    }
    documment = template.render(context, request)
    return (HttpResponse(documment))

# /////////////////////////////////////////////////////////////////

def about(request):
    template = loader.get_template('about.html')
    context = {
        'error_url': request.path,
    }
    documment = template.render(context, request)
    return (HttpResponse(documment))

