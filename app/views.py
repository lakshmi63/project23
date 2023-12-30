from django.shortcuts import render

from app.models import *
from django.http import HttpResponse

# Create your views here.
def create_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        qlto=Topic.objects.all()
        d={'topic':qlto}
        return render(request,'display_topic.html',d)
    return render(request,'create_topic.html')

def create_webpage(request):
    qlto=Topic.objects.all()
    d={'topic':qlto}
    if request.method=='POST':
        tn=request.POST['tn']
        wn=request.POST['n']
        ur=request.POST['u']
        em=request.POST['e']

        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=wn,url=ur,email=em)[0]
        WO.save()
        qlwo=Webpage.objects.all()
        d1={'webpage':qlwo}
        return render(request,'display_webpage.html',d1)
        
    
    return render(request,'create_webpage.html',d)