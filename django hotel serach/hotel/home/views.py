from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.


def get_hotel(request):
    try:
        hotel_obj=Hotel.objects.all()
        payload=[]
        for hotel_objs in hotel_obj:
            payload.append({
                'hotel_name':hotel_obj.hotel_name,
                'hotel_price':hotel_obj.hotel_price,
                'hotel_description':hotel_obj.hotel_description,
                'banner_image':hotel_obj.banner_image
            })
        return JsonResponse(payload,safe=False)    
    except Exception as e:
        print(e)
    return JsonResponse({'message':'something is wrong'})    

