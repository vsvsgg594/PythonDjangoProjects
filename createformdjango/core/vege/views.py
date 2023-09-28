from django.shortcuts import render
from .models import *

# Create your views here.
def receipes(request):
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_des=data.get('reeceipe_des')
        # receipe_img=data.FILES.get('receipe_image')
        print(receipe_name)
        print(receipe_des)
        # print(receipe_img)
        Receipes.objects.create(
            receipe_name=receipe_name,
            receipe_des=receipe_des,
                #   receipe_img

            )

    return render(request,"receipes.html")
