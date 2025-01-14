from django.shortcuts import render, redirect
from .models import Task
# Create your views here.
# Django ORM - Django Object Relational Management
# Tasks.objects.all()
def home_page(request):
    vazifalar = Task.objects.all()
    tugatilgan_vazifalar = Task.objects.filter(status='tugallangan')
    tugatilmagan_vazifalar = Task.objects.filter(status='tugallanmagan')

    if request.method=="POST":
        newtask = request.POST['newtask']
        Task.objects.create(title=newtask)
        redirect('home')

    context = {
        'tasks': vazifalar,
        'finished': tugatilgan_vazifalar,
        'unfinished': tugatilmagan_vazifalar
    }

    return render(request, template_name='index.html', context=context)

