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
app_name='comic'
urlpatterns = [
    #re_path(r'^create',views.newGroupCreate,name='NewGroupCreate'),
    re_path(r'^home',views.HomeCV,name='HomeCV'),
    re_path(r'^cartoon',views.CartoonCV,name='CartoonCV'),
    re_path(r'^game',views.GameCV,name='GameCV'),
    re_path(r'^article',views.ArticleCV,name='ArticleCV'),
    re_path(r'^user',views.UserCV,name='UserCV'),
    re_path(r'^serach',views.SearchCV,name='SearchCV'),
    re_path(r'^update',views.UpdateCV,name='UpdateCV'),
    re_path(r'^doing',views.DodingCV,name='DodingCV'),
    re_path(r'^label',views.LabelCV,name='LabelCV'),
    #
    re_path(r'^home',TemplateView.as_view(template_name="comic/HomeC.html"),name='Others_done'),   # 显示最基础的模板
    re_path(r'',TemplateView.as_view(template_name="comic/HomeC.html"),name='Others_done'),   # 显示最基础的模板
    re_path(r'',TemplateView.as_view(template_name="comic/test.html"),name='Others_done'),   # 显示最基础的模板

]
