from django.shortcuts import render

# Create your views here.
def HomeCV(request):
    return render(request, 'comic/HomeC.html')
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
