from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,"display.html")

def loginpage(request):
    return render(request ,"loginpage.html")