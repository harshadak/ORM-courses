from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from time import gmtime, strftime, localtime
from django.contrib import messages
from models import * # Need this in order to run queries
from django.core.urlresolvers import reverse


def index(request):
    context = {
        "courses_all" : Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('index'))
        else:
            Course.objects.create(course_name = request.POST["name"], desc = request.POST["descript"])
            return redirect(reverse('index'))

def destroy(request, id):
    context = {
        "course" : Course.objects.get(id = id)
    }
    return render(request, 'courses/delete.html', context)

def confirm(request, id):
    delete_course = Course.objects.get(id = id)
    delete_course.delete()
    return redirect(reverse('index'))
