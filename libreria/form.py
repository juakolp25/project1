from pyexpat import model
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextImput(attrs={"class":"textimput"}))

    class Meta:
        model = Contacto
        fields = '__all__'