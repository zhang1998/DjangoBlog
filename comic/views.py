from django.shortcuts import render
from newGroup.models import ImageSt
# Create your views here.
def HomeCV(request):
    qu1=ImageSt.objects.all()
    print(qu1)
    return render(request, 'comic/HomeC.html',{"columns":qu1})
def DodingCV(request):
    return render(request, 'comic/DodingC.html')
def LabelCV(request):
    return render(request, 'comic/LabelC.html')
def CartoonCV(request):
    return render(request, 'comic/CartoonC.html')
def GameCV(request):
    return render(request, 'comic/GameC.html')
def ArticleCV(request):
    return render(request, 'comic/ArticleC.html')
def UserCV(request):
    return render(request, 'comic/UserC.html')
def SearchCV(request):
    return render(request, 'comic/SearchC.html')
def UpdateCV(request):
    return render(request, 'comic/UpdateC.html')
