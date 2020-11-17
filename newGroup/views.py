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
    q = request.POST['input']
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'newGroup/results.html', {'error_msg': error_msg})
    #测试的内容 是 test2
    post_list = ImageSt.objects.filter(title__contains=q)
    #return HttpResponse("1")
    return render(request, 'newGroup/results.html', {'error_msg': error_msg,'post_list': post_list})
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
                groupsId=new_Groups.id
                #return HttpResponseRedirect("/newGroup/choose/")
                return HttpResponseRedirect(reverse('newGroup:newGroupChoose',args=(groupsId,)))

            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("3")


#选择图片的源 组
def newGroupChoose(request,groupsId):
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
                return HttpResponseRedirect(reverse('newGroup:newGroupColumn',args=(imageGroups,groupsId,)))
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


def newGroupColumn(request,imageGroups,groupsId):
    if request.method=="POST":
        article_post_form = editorRnepy(data=request.POST)
        if article_post_form.is_valid():
            html=''
            saimageId=0
            showOr=0
            TextContent=''
            saImageLocal=imageGroups
            stem="show"
            mmm=article_post_form.cleaned_data['body'].split('\n')
            saimageId=1
            GroupsNam=Groups.objects.get(id=groupsId)
            print(type(GroupsNam))
            try:
                for n in mmm:

                #进行 行处理 与另一个数据库的存入
                #i创建相关的groups 与之对应
                    print("首行的n:"+n)

                        # 匹配到 show 修改 image的id
                    if n.find(stem)!=-1:
                        print("YES")
                        print("n:")
                        print(n)
                        spli=n.split(' ')
                        print(spli)
                        saimageId=spli[1]
                        continue
                    else :
                        TextContent=n
                        #读取文字内容
                        #其他都是递加存入 生成了数据对象
                        showOr=showOr+1
                        print("///////////////////////////////////")
                        p=Group(imageId=saimageId,imageLoca=saImageLocal,showOrder=showOr,textContent=TextContent,groups=GroupsNam)
                        print("///////////////////////////////////")

                    p.save()
                return HttpResponse("1")
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("3")
    else:#下面是get的内容
        article_post_form = editorRnepy()
        qu1=Group.objects.filter(groups=imageGroups)

        #article_columns = request.user.article_column.all()
        return render(request, "newGroup/NewGroupColumnpr.html",{"form":article_post_form,"columns":qu1})

def morefunction(request):
    return render(request, 'newGroup/morefunctionpr.html')
