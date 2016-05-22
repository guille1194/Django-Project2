from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from .models import Promotor, Promovido

class Registro(forms.Form):
    promovido_id = forms.IntegerField()
    promovido_nombre = forms.CharField(max_length=64)
    promotor = forms.ModelChoiceField(Promotor.objects, empty_label= "Selecciona Promotor")
    voto = forms.NullBooleanField()

class PromotorForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    class Meta:
        fields = ['email', 'username', 'first_name', 'last_name', 'password1',
                  'password2']
        model = User
