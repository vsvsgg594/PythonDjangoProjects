from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples=[{'name' : 'vikash','age':23},
             {'name' : 'vikash','age':23},
             {'name' : 'vikash','age':23},
             {'name' : 'vikash','age':23},
             {'name' : 'vikash','age':23}]
    vagetables=["pumkin","cucumber","karrot"]

    for people in peoples:
        print(people)





    return render(request,"index.html",context={'page':'Document','peoples':peoples,'vagetables':vagetables})
def contact(request):
    context={'page':'contact'}
    return render(request,"contact.html",context)
def about(request):
    context={'page':'about'}
    return render(request,"about.html",context)

   
