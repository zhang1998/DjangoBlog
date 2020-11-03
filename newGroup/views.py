from django.shortcuts import render
from django.http import HttpResponse

from .models import Group,Groups,ImageSt
from .forms import *
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
#实现image的搜索 主要是搜索名字
def search(request):
    q = request.GET.get('search_content')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'newGroup/errors.html', {'error_msg': error_msg})
    #测试的内容 是 test2
    post_list = ImageSt.objects.filter(title__contains=q)
    return render(request, 'newGroup/results.html', {'error_msg': error_msg,
                                               'post_list': post_list})
def newGroup(request):
    if request.method=="GET":
        create_form=NewGroupForm(request.POST)#4
        return render(request,'newGroup/newGroup1.html',{"form":create_form})
    if request.method=="POST":
        create_form=NewGroupForm(request.POST)#4
        if create_form.is_valid():
            reData=create_form.cleaned_data
            groups =Groups(title=reData['title'])
            groups.save()
        print(create_form)
        return HttpResponse("ye")
