"""DjPra1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views



#from django.conf.urls import url,include
urlpatterns = [
    re_path(r'^search/$',views.search,name='search'),
    re_path(r'^newGroup',views.newGroup,name='newGroup'),
    #test
    # start 练习部分的内容
    re_path(r'^base',views.testbase,name='testbase'),
    re_path(r'^guide',views.testGuide,name='testGuide'),
    re_path(r'^home',views.homePage,name='homePage'),
    re_path(r'^showimage',views.showImage,name='showImage'),

    re_path(r'^create',views.newGroupCreate,name='NewGroupCreate'),
    path('choose/<int:Groups>/',views.newGroupChoose,name='newGroupChoose'),
    #path('articles/<int:year>/', views.year_archive, name='news-year-archive'),
    #path('articles/<int:year>/', views.year_archive, name='news-year-archive'),
    re_path(r'^column',views.newGroupColumn,name='newGroupColumn'),

    re_path(r'more',views.morefunction,name='morefunction'),


    #end
    #test 部分




    #re_path(r'',TemplateView.as_view(template_name="newGroup/newGroup1.html"),name='newGroup1'),
    #re_path(r'',TemplateView.as_view(template_name="newGroup/newGroup_test1.html"),name='test_newGroup'),
    #re_path(r'',TemplateView.as_view(template_name="newGroup/newGroup_test.html"),name='test_newGroup'),


    #re_path(r'',views.text_content,name='test'),


]
