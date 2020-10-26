from django.shortcuts import render
from .models import Group,Groups
# Create your views here.
def text_content(request):
    #text=Group.objects.all()

    #筛选组的id
    qu1=Groups.objects.filter(title='testshow')
    qu1=qu1.get()
    qu1=qu1.id
    #获得 组对应的内容
    qu1=Group.objects.filter(groups=qu1)

    #对组对应的内容进行排序
    columns=qu1.order_by('showOrder')
    #传递组的内容

    #传递 image的位置

    qu1=Groups.objects.filter(title='testshow')
    qu1=qu1.get()
    qu1=qu1.id
    qu1=Group.objects.filter(groups=qu1)

    return render(request,"newGroup/test.html",{"columns":columns})
