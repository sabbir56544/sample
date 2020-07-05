from django.shortcuts import render
from .models import About

def about(requset):
    about_list = About.objects.all()
    context = {
        'about' : about_list
    }
    return render(requset, 'about.html', context)