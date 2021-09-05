import random

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def sayhello(request):
    return HttpResponse('hi django')
def hello2(request,username):
    return HttpResponse('hello '+ username )
def hello3(request,username):
    now =datetime.now()
    return render(request, 'hello3.html',locals())
def hello4(request,username):
    now = datetime.now()
    return render(request, 'hello4.html',locals())
def dice2(request):
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    no3 = random.randint(1,6)

    return render(request,'dice.html', locals())
def show(request):
    person1 = {'name': 'ali', 'age':12, 'country':'MY'}
    person2 = {'name': 'yb', 'age': 15, 'country': 'HK'}
    person3 = {'name': 'sansan', 'age': 11, 'country': 'sg'}
    persons = [person1, person2, person3]
    return render(request,'show.html',locals())
def djget(request):
    name = request.GET['name']
    city = request.GET['city']
    return render(request,'djget.html',locals())
def djpost(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username == 'yb' and password =='123':
            return HttpResponse('welcome to django')
        else:
            return HttpResponse('failed')
    else:
        return render(request, 'djpost.html', locals())
