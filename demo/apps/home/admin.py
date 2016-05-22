from django.contrib import admin
from django.contrib.auth.models import User
from .models import Promotor, Promovido
from django import forms
from .forms import Registro, PromotorForm
# Register your models here.

admin.site.register(Promovido)
admin.site.register(Promotor)
