from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view()

def home(request):
    return Response({
        'status':400,
        'message':'this is api called',
    })