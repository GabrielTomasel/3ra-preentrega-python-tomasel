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
def courses(request, id=None):
    if id is not None:
        result = Course.objects.filter(Q(id__icontains=id))
    else:
        result = Course.objects.all()
    if len(result) > 0:
        return render(request, "courses_search.html", {"search": result, "id": id})
    else:
        return render(request, "courses_search.html", {"error": id})

@login_required
def courses_form(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form_cleaned = form.cleaned_data
            course = Course (course_id = form_cleaned['course_id'], course_type = form_cleaned['course_type'])
            course.save()
            return redirect('/courses')
    else:
        form = CourseForm()
    return render(request, "courses_form.html" , {'form':form})

@login_required
def courses_search(request):
    if request.GET["search"]:
        result = Course.objects.filter(Q(course_id__icontains = request.GET["search"])|Q(course_type__icontains = request.GET["search"]))
        if len(result)>0:
            return render(request, "courses_search.html", {"search": result})
        else:
            return render(request, "courses_search.html", {"error": request.GET["search"]})
    else:
        result = "Search data missing"
    return HttpResponse(result)


class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courses')
    context_object_name = 'course'
    template_name = 'courses_delete.html'
