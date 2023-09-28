from django.shortcuts import render

# Create your views here.

def displayimage(request):
    return render(request ,'index.html')