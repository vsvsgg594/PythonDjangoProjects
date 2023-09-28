from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hi this new dajngo server")


def contact(request):
    return HttpResponse("hey thsi is contact")

