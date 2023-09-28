from django.shortcuts import render,redirect
from .form import ImageForm
from .models import Imageuploader
# Create your views here.
def display(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            return redirect('/index/')    

    form=ImageForm()
    img=Imageuploader.objects.all()
    return render(request , "index.html", {'img':img,'form':form})