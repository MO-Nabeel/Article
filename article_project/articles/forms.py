from django import forms
from .models import Article

class Article_Form(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','author']