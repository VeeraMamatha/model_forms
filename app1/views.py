from django.shortcuts import render
from app1.models import *
from app1.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    ETFO=Topicform()
    d={'etfo':ETFO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('topic table is created')
        else:
            return HttpResponse('topic table is not created')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=Webpageform()
    d={'ewfo':EWFO}
    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('webpage table is created')
        else:
            return HttpResponse('webpage table is not created')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EAFO=Accessrecordform()
    d={'eafo':EAFO}
    if request.method=='POST':
        AFDO=Accessrecordform(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('accessrecord table is created')
        else:
            return HttpResponse('accessrecord table is not created')

    return render(request,'insert_accessrecord.html',d)
