from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
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
def testbase(request):
    return render(request, 'newGroup/testbasepr.html')
def testGuide(request):
    return render(request, 'newGroup/Guidepr.html')
def homePage(request):
    return render(request, 'newGroup/homePagepr.html')
def showImage(request):
    return render(request, 'newGroup/showImagepr.html')


def newGroupCreate(request):
    if request.method == "GET":
        create_form= NewGroupForm()
        return render(request, 'newGroup/NewGroupCreatepr.html' ,{"form":create_form})
    if request.method == "POST":
        post_form = createGroups(data=request.POST)
        if post_form.is_valid():
            cd = post_form.cleaned_data
            try:
                new_Groups=post_form.save(commit=False)
                #new_article.column =
                new_Groups.save()
                GroupsId=new_Groups.id
                #return HttpResponseRedirect("/newGroup/choose/")
                return HttpResponseRedirect(reverse('newGroup:newGroupChoose',args=(GroupsId,)))

            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("3")


#选择图片的源 组
def newGroupChoose(request,Groups):
    if request.method == "GET":
        create_form= ChooseImageGroups()
        return render(request, 'newGroup/NewGroupChoosepr.html',{"form":create_form})
    if request.method == "POST":
        post_form = ChooseImageGroups(data=request.POST)
        imageGroups=0
        if post_form.is_valid():
            imageGroups=1
            try:
                #imageGroups=post_form.fields['ImageGroup']
                imageGroups=post_form.cleaned_data
                imageGroups=imageGroups['ImageGroup']
                #f.fields['name']
                #return HttpResponseRedirect("/newGroup/choose/")
                return HttpResponseRedirect(reverse('newGroup:newGroupColumn',args=(imageGroups,Groups,)))
            except Exception as e:

                return HttpResponse(imageGroups['ImageGroup'])

        else:
            return HttpResponse("3")


'''
处理 column的函数

1. 对输入的内容进行匹配 并按照相应的规则写入 数据表

'''
def coulumnSave(editorTest):
    # 分行
    for e in editorTest.objects.all():
        print(e.body.split('\n'))

    # 找到了image就切换 相应的image


def newGroupColumn(request,imageGroups,Groups):
    if request.method=="POST":
        article_post_form = editorRnepy(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article=article_post_form.save(commit=False)
                #new_article.column =
                new_article.save()

                #进行 行处理 与另一个数据库的存入
                #i创建相关的groups 与之对应
                #每一个的处理
                for e in  article_post_form.objects.all():
                    m=e.body.split('\n')
                    saimageId=0
                    saImageLocal=0
                    showOr=0
                    TextContent=''
                    Groups=''
                    for n in m:# 每一段内容
                        #进行匹配和处理
                        print(n)

                        # 匹配到 show 修改 image的id
                        #其他都是递加

                return HttpResponse("1")
            except:
                return HttpResponse("2")
        else:
            return HttpResponse("3")
    else:
        article_post_form = editorRnepy()
        #article_columns = request.user.article_column.all()
        return render(request, "newGroup/NewGroupColumnpr.html",{"form":article_post_form})

def morefunction(request):
    return render(request, 'newGroup/morefunctionpr.html')
