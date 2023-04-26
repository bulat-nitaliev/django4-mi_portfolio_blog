from django.shortcuts import render
from .models import Project
import random

def home(request):
	projects = Project.objects.all()
	return render(request,'portfolio/home.html',{'projects':projects})

def about(request):
	return render(request,'portfolio/about.html')

def pasword(request):
	return render(request,'portfolio/pasword_home.html')

def your_pasword(request):
    pasword = ''
    len = request.GET.get('lenght',12)
    character = list('qwertyuiopasdfghjklzxcvbnm')
    
    if request.GET.get('uppercase'):
        character.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('nambers'):
        character.extend(list('1234567890'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()_'))
    for i in range(int(len)):
        pasword += random.choice(character)
    return render(request,'portfolio/your_pasword.html',{'pasword':pasword})


