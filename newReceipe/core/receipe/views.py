from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.core.paginator import Paginator
# Create your views here.
def receipe(request):
    if request.method=="POST":
        data=request.POST
        # print(data)
        receipe_name=data.get('receipe_name')
        receipe_des=data.get("receipe_des")
        print(receipe_name)
        print(receipe_des)
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_des=receipe_des,

        )
        return redirect('/receipe')
    Queryset=Receipe.objects.all()
    context={'receipe':Queryset}    

    return render(request,"receipe.html",context)

def update_receipe(request,id):
     Queryset=Receipe.objects.get(id=id)
     context={'receipe':Queryset}
     if request.method=="POST":
         data=request.POST
         receipe_name=data.get('receipe_name')
         receipe_des=data.get('receipe_des')
         Queryset.receipe_name=receipe_name
         Queryset.receipe_des=receipe_des
         Queryset.save()
         return redirect('/receipe/')
     return render(request ,'update_receipe.html' ,context)


def delete_receipe(request,id):
    Queryset=Receipe.objects.get(id=id)
    Queryset.delete()    
    return redirect('/receipe')
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('passowrd')
        if not User.objects.filter(username=username).exists():
            messages.info(request,"invalied username")
            return redirect('/login/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request, "invalied password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/receipe/')

    return render(request ,'loginpage.html')

def reistationpage(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request ,"username already exits")
            return redirect('/resistation/')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username

        )
        user.set_password(password)
        user.save()
        messages.info(request ,"Account created successfully")
        return redirect('/resistation/')
    return render(request ,'reistationpage.html')
from django.db.models import Q

def get_students(request):
    queryset=Student.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(
            Q(student_name__icontains=search)|
            Q(department__department__icontains=search)| 
            Q(student_id__student_id__icontains=search)

        )
     
    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    return render(request ,'studentsdata.html',{'queryset':page_obj })