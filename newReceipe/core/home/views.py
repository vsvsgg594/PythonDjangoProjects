from django.shortcuts import render

# from django.http import HttpResponse
# Create your views here.
def home(request):
    persons=[{'name':'vikash','age':23,'address':'Bihar'},
             {'name':'vijay','age':34,'address':'Bihar'},
             {'name':'vikash','age':23,'address':'Bihar'},
             {'name':'vijay','age':34,'address':'Bihar'},
             {'name':'vikash','age':23,'address':'Bihar'},
             {'name':'vijay','age':34,'address':'Bihar'},
             {'name':'vikash','age':23,'address':'Bihar'},
             {'name':'vijay','age':34,'address':'Bihar'},
             {'name':'vikash','age':23,'address':'Bihar'},
             {'name':'vijay','age':34,'address':'Bihar'}]
    for person in persons:
        print(person)
    return render(request ,"index.html",context={'persons':persons})
def contact(request):
    context={'page':'contact'}
    return render(request,"contact.html" ,context)
def about(request):
    context={'page':'about'}
    return render(request,"about.html",context)
