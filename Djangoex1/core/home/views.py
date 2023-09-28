from django.shortcuts import render

# Create your views here.
def home(request):
    person=[{'name':'vikash','age':34},{'name':'vikash','age':34},{'name':'vikash','age':34}]
    for persons in person:
        print(person)
    return render(request ,"index.html", context={'person':person})    
