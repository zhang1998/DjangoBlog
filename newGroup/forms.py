from django import forms
from .models import *



class ArticlePostForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=("imageId","showOrder")
