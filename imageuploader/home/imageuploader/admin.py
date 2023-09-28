from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ImageUploader)

class ImageAdmin(admin.ModelAdmin):
    list_display =['id','photo','date']
