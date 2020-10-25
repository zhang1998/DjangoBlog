from django.shortcuts import render
from .models import Group
# Create your views here.
def text_content(request):
    text=Group.objects.all()
    return render(request,"newGroup/test.html",{"texts":text})
