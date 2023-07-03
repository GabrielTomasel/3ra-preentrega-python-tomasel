from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import * 
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *


@login_required
def comunications(request, id=None):
    if id is not None:
        result = Comunication.objects.filter(Q(id__icontains=id))
    else:
        result = Comunication.objects.all()
    if len(result) > 0:
        return render(request, "comunications_search.html", {"search": result, "id": id})
    else:
        return render(request, "comunications_search.html", {"error": id})

@login_required
def comunications_form(request):
    if request.method == 'POST':
        comunication = Comunication(message_name = request.POST['message_name'], message = request.POST['message'])
        comunication.save()
        return redirect('/comunications/')
    else:
        pass
    return render(request,'comunications_form.html')

@login_required
def comunications_search(request):
    if request.GET["search"]:
        result = Comunication.objects.filter(Q(comunication_id__icontains = request.GET["search"])|Q(comunication_username__icontains = request.GET["search"]))
        if len(result)>0:
            return render(request, "comunications_search.html", {"search": result})
        else:
            return render(request, "comunications_search.html", {"error": request.GET["search"]})
    else:
        result = "Search data missing"
    return HttpResponse(result)


class DeleteComunication(LoginRequiredMixin, DeleteView):
    model = Comunication
    success_url = reverse_lazy('comunications')
    context_object_name = 'comunication'
    template_name = 'comunications_delete.html'