from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")


def success_page(request):
    return HttpResponse("<h1>hey this is success page<h1>")
