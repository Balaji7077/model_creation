from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)

def insert_topic(request):
    tn=input('enter tn')

    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()

    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)


def display_webpages(request):
    QLWO=Webpage.objects.all()

    QLWO=Webpage.objects.all().order_by('topic_name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())

    QLWO=Webpage.objects.filter(name__startswith='R')
    QLWO=Webpage.objects.filter(url__endswith='in')
    QLWO=Webpage.objects.filter(name__contains='o')
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket')& Q(name__startswith='R'))
    QLWO=Webpage.objects.filter(topic_name='Cricket',name__startswith='k')
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket')|(Q(name__endswith='i')))
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket')&(Q(Email__startswith='rahul')))
    QLWO=Webpage.objects.filter(name__startswith='g',url__endswith='in')
    

    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)

def insert_webpage(request):
    tn = input("ENter the topic name")
    n=input("Enter the name")
    u=input("Enter the url")
    e=input("enter the email")
    To=Topic.objects.get(topic_name=tn)

    NWO=Webpage.objects.get_or_create(topic_name=To,name=n,url=u,Email=e)[0]
    NWO.save()

    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)

def display_acessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'acess':QLAO}
    return render(request,'display_acessrecord.html')

def insert_acessrecord(request):
    nm = input("Enter the name of the webpage: ")
    dt = input("Enter the date: ")
    at = input("Enter the author: ")

    # Assuming Webpage model has a 'topic_name' field
    wb = Webpage.objects.get(name='rahul')

    ac = AccessRecord.objects.get_or_create(name=wb, date=dt, author=at)[0]
    ac.save()

    QLAO = AccessRecord.objects.all()
    d = {'acess': QLAO}
    return render(request, 'display_acessrecord.html', d)

def update(request):
        QLWO=Webpage.objects.all()
        Webpage.objects.filter(topic_name='Cricket').update(name='pandya')
        d={'webpages':QLWO}
        return render(request,'display_webpages.html',d)