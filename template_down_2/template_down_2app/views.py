from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    obj = Place.objects.all()
    obj1 = Meetteam.objects.all()
    return render(request,'index.html',{'obj':obj,'obj1':obj1})
