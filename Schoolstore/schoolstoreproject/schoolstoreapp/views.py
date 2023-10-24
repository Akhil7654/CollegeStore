from django.shortcuts import render

from schoolstoreapp.models import Box,Testimonial


# Create your views here.


def home(request):
    obj=Box.objects.all()
    obj2=Testimonial.objects.all()
    return render(request,"home.html",{'key1':obj,'res2':obj2})
