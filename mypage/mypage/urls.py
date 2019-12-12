"""mypage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from mypage.views import *

urlpatterns = [
    path('', blog_list, name='index'),
    path('admin/', admin.site.urls),
    path('blog/list/', blog_list, name='blog_list'),
    path('blog/create/', blog_create, name='blog_create'),
    path('blog/view/<int:id>/', blog_view, name='blog_view'),

    # Accounts urls
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]
