from django.shortcuts import render
from .models import *

# Create your views here.
def page_first(request):
    return render(request ,"firstpage.html")

def get_studentsdata(request):
    queryset=Student.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('serach')
        queryset=queryset.filter(student_name__icontains=search)
        
    return render(request , "display.html" ,context={'queryset':queryset})
