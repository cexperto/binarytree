"""binarytree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path
from theapi import views


def index(request):
    return HttpResponse('binary tree API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('create', views.create_tree, name='create'),
    path('binarytree', views.binary_tree, name='binarytree')
]
