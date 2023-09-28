from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def dis(request):
    return render(request ,"index.html")


def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        username=request.POST.get('username')
        password=request.POST.get('password')


        user=User.objects.create(
            first_name=first_name,
            username=username
        )
        user=User.objects.filter(username=username)
        if user.exists():
            print("user exites")
            return redirect('/register/')
        
        
        user.set_password(password)
        user.save()
        return redirect('/register/')

        
    return render(request ,"register.html")
