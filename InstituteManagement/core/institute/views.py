from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    if request.method=="POST":
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        standard=data.get('standard')
        print(name)
        print(email)
        print(standard)
        Student.objects.create(
            name=name,
            email=email,
            standard=standard,

        )
        return redirect('/index')
    Queryset=Student.objects.all()
    context={'index':Queryset}   
    return render(request, 'index.html',context)
def delete_index(request,id):
    QuerySet=Student.objects.get(id=id)
    QuerySet.delete()
    return redirect('/index')  

def update_index(request,id):
    Queryset=Student.objects.get(id=id)
    context={'index':Queryset}
    if request.method=="POST":
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        standard=data.get('standard')
        Queryset.name=name
        Queryset.email=email
        Queryset.standard=standard
        Queryset.save()
        return redirect('/index/')
    return render(request ,"update.html",context)

 


    