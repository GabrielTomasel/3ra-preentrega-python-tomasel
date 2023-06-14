from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import * 
from django.db.models import Q
from django.shortcuts import render
from .forms import *


def index(request):
    template = loader.get_template('home.html')
    documment = template.render()
    print("Index")
    return (HttpResponse(documment))


def students(request):
    template = loader.get_template('students.html')
    documment = template.render()
    return (HttpResponse(documment))

def students_form(request):
    if request.method == 'POST':
        student = Student(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        student.save()
        # return render(request,'preentrega3/home.html')
    else:
        pass
    return render(request,'preentrega3/students_form.html')

def students_search(request):
    if request.GET["search"]:
        result = Student.objects.filter(Q(first_name__icontains = request.GET["search"])|Q(last_name__icontains = request.GET["search"])|Q(email__icontains = request.GET["search"]))
        if len(result)>0:
            return render(request,"students_search.html",{"search": result})
        else:
            return render(request,"students_search.html",{"error": "No courses found"})
    else:
        result = "Search data missing"
    return HttpResponse(result)


def courses(request):
    template = loader.get_template('courses.html')
    documment = template.render()
    return (HttpResponse(documment))

def courses_form(request):
    print("Courses Form")
    if request.method == 'POST':
        print("post")
        form = CourseForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            form_cleaned = form.cleaned_data
            print("Cleaned")
            course = Course (course_id = form_cleaned['course_id'], course_type = form_cleaned['course_type'])
            course.save()
            print("Saved")
            # return render(request, 'preentrega3/home.html')
    else:
        print("Post missing")
        form = CourseForm()
    return render(request, "courses_form.html" , {'form':form})

def courses_search(request):
    if request.GET["search"]:
        result = Course.objects.filter(Q(course_id__icontains = request.GET["search"])|Q(course_type__icontains = request.GET["search"]))
        if len(result)>0:
            return render(request, "courses_search.html", {"search": result})
        else:
            return render(request, "courses_search.html", {"error": "No courses found"})
    else:
        result = "Search data missing"
    return HttpResponse(result)


def professors_form(request):
    if request.method == 'POST':
        professor = Professor(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        professor.save()
        # return render(request,'preentrega3/home.html')
    else:
        pass
    return render(request,'preentrega3/professors_form.html')

def professors_search(request):
    print("Professor Search")
    if request.GET["search"]:
        result = Professor.objects.filter(Q(first_name__icontains = request.GET["search"])|Q(last_name__icontains = request.GET["search"])|Q(email__icontains = request.GET["search"]))
        print(result)
        print(len(result))
        if len(result)>0:
            return render(request, "professors_search.html", {"search": result})
        else:
            return render(request, "professors_search.html", {"error": "No Professors found"})
    else:
        result = "Search data missing"
    return HttpResponse(result)

    
