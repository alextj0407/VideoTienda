from django import forms
from .models import Actor

class actor_form(forms.ModelForm):
    class Meta:
        model =  Actor
        fields='__all__'
