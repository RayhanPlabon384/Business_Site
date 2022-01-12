from django.shortcuts import render
from .models import About,Slider,Client

def home(request):
    aboutdata = About.objects.all()[0]
    sliderdata = Slider.objects.all()
    clientdata = Client.objects.all()
    context = {
        'about':aboutdata,
        'slider':sliderdata,
        'client':clientdata
    }
    return render(request,'homepage.html',context)

def about(request):
    return render(request,'about.html')

