from django import forms
from .models import *



class ArticlePostForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=("imageId","showOrder")
class NewGroupForm(forms.Form):

    title=forms.CharField(max_length=300,label='title')
    originImageGroups=forms.IntegerField(label='使用的组序号')
