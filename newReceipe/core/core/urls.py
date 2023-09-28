"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from receipe.views import *

urlpatterns = [
    path('', home),
    path('receipe/',receipe,name="receipe"),
    path('delete_receipe/<id>/' ,delete_receipe ,name="delete_receipe"),
    path('update_receipe/<id>/', update_receipe ,name="update_receipe"),
    path('contact/' , contact ,name="contact"),
    path('about/', about ,name="about"),
    path('login/', loginpage , name="loginpage"),
    path('students/' , get_students ,name="get_students"),
    path('resistation/', reistationpage ,name="reistationpage"),
    path("admin/", admin.site.urls),
]
