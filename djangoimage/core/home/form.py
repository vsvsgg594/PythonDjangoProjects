from django import forms
from .models import Imageuploader

class ImageForm(forms.ModelForm):
    class Meta:
        model=Imageuploader
        fields='__all__'
        labels={'photo':''}
        