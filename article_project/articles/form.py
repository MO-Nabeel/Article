from django import forms
from .models import Article

class Article_Form(forms.Modelform):
    class Meta:
        model = Article
        fields = ['title','content','author']