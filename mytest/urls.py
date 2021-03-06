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



#from django.conf.urls import url,include
urlpatterns = [
    re_path(r'',TemplateView.as_view(template_name="mytest/home.html"),name='test'),   # 显示最基础的模板
    re_path(r'',TemplateView.as_view(template_name="mytest/index.html"),name='test'),   # 显示最基础的模板
    re_path(r'',TemplateView.as_view(template_name="mytest/testjs2.html"),name='test'),   # 显示最基础的模板
    re_path(r'',TemplateView.as_view(template_name="mytest/testjs.html"),name='test'),   # 显示最基础的模板
    re_path(r'',TemplateView.as_view(template_name="mytest/home.html"),name='test'),   # 显示最基础的模板


]
