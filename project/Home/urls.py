"""
URL configuration for ToDolistApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('features',views.features,name='features'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='home'),
    path('send',views.send,name='send'),
    path('todo',views.todo,name='todo'),
    path('addtask',views.addtask,name='add'),
    path('show',views.show,name='show'),
    path('get',views.get,name='get'),
    path('delete',views.delete_task,name='delete'),
    path('edit',views.edit,name='edit'),
    path('RecordEdited',views.RecordEdited,name='record'),
    path('priority',views.priority,name='priority'),
    path('complete',views.complete,name='complete'),
    
    
]
