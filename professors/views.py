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
def professors(request, id=None):
    if id is not None:
        result = Professor.objects.filter(Q(id__icontains=id))
    else:
        result = Professor.objects.all()
    if len(result) > 0:
        return render(request, "professors_search.html", {"search": result, "id": id})
    else:
        return render(request, "professors_search.html", {"error": id})

@login_required
def professors_form(request):
    if request.method == 'POST':
        professor = Professor(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        professor.save()
        return redirect('/professors/')
    else:
        pass
    return render(request,'professors_form.html')

@login_required
def professors_search(request):
    print("Professor Search")
    if request.GET["search"]:
        result = Professor.objects.filter(Q(first_name__icontains = request.GET["search"])|Q(last_name__icontains = request.GET["search"])|Q(email__icontains = request.GET["search"]))
        print(result)
        print(len(result))
        if len(result)>0:
            return render(request, "professors_search.html", {"search": result})
        else:
            return render(request, "professors_search.html", {"error": request.GET["search"]})
    else:
        result = "Search data missing"
    return HttpResponse(result)


class DeleteProfessor(LoginRequiredMixin, DeleteView):
    model = Professor
    success_url = reverse_lazy('professors')
    context_object_name = 'professor'
    template_name = 'professors_delete.html'