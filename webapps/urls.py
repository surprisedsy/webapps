"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

import helloweb.views as helloweb_views
import emaillist.views as emaillist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloweb/hello', helloweb_views.hello),   # 실행이 아니기 때문에 hello() 안씀
    path('helloweb/tags', helloweb_views.tags),
    path('helloweb/join', helloweb_views.join),


    path('emaillist/', emaillist_views.index),

]
