from django import forms
from django.forms import ModelForm
from .models import livro

class LivroForm(ModelForm):
  class Meta:
    model = livro
    fields = ['titulo', 'status']