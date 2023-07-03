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
def students(request, id=None):
    if id is not None:
        result = Student.objects.filter(Q(id__icontains=id))
    else:
        result = Student.objects.all()
    if len(result) > 0:
        return render(request, "students_search.html", {"search": result, "id": id})
    else:
        return render(request, "students_search.html", {"error": id})

@login_required
def students_form(request):
    if request.method == 'POST':
        student = Student(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        student.save()
        return redirect('/students/')
    else:
        pass
    return render(request,'students_form.html')

@login_required
def students_search(request):
    if request.GET["search"]:
        result = Student.objects.filter(Q(first_name__icontains = request.GET["search"])|Q(last_name__icontains = request.GET["search"])|Q(email__icontains = request.GET["search"]))
        if len(result)>0:
            return render(request,"students_search.html",{"search": result})
        else:
            return render(request,"students_search.html",{"error": request.GET["search"]})
    else:
        result = "Search data missing"
    return HttpResponse(result)


class DeleteStudent(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students')
    context_object_name = 'student'
    template_name = 'students_delete.html'
