from django.shortcuts import render

# Create your views here.
def display(request):
    return render(request ,"display.html")
def loginpages(request):
    return render(request , "loginpages.html")