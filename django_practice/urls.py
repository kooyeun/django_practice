"""django_practice URL Configuration

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
from django.urls import path

import helloworld.views as helloworldviews
import emaillist01.views as emaillist01views
import emaillist02.views as emaillist02views
import guestbook01.views as guestbook01views
import guestbook02.views as guestbook02views

urlpatterns = [
    path('', helloworldviews.main),
    path('form/', helloworldviews.form),
    path('join', helloworldviews.join),
    path('hello1/', helloworldviews.hello1),
    path('tags/', helloworldviews.tags),

    path('emaillist01/', emaillist01views.index),
    path('emaillist01/form', emaillist01views.form),
    path('emaillist01/add', emaillist01views.add),

    path('emaillist02/', emaillist02views.index),
    path('emaillist02/form', emaillist02views.form),
    path('emaillist02/add', emaillist02views.add),

    path('guestbook01/', guestbook01views.index),
    path('guestbook01/add', guestbook01views.guestAdd),
    path('guestbook01/deleteForm', guestbook01views.deleteForm),
    path('guestbook01/delete', guestbook01views.guestDelete),

    path('guestbook02/', guestbook02views.index),
    path('guestbook02/add', guestbook02views.guestAdd),
    path('guestbook02/deleteForm', guestbook02views.deleteForm),
    path('guestbook02/delete', guestbook02views.guestDelete),

    path('admin/', admin.site.urls),
]

