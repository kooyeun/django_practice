from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from guestbook01 import models


def index(request):
    results=models.findall()
    guestList={'guest_list': results}
    return render(request,'guestbook01/index.html',guestList)

def guestAdd(request):
    models.insert(request.POST["name"],request.POST["password"],request.POST["message"])
    return HttpResponseRedirect("/guestbook01")

def deleteForm(request):
    print("deleteForm=====deleteForm======deleteForm=====deleteForm")
    no=request.GET["no"]
    print("no="+no)
    num={'no':no}
    return render(request,"guestbook01/deleteform.html",num)

def guestDelete(request):
    print("======guestDelete======guestDelete======guestDelete======guestDelete")
    no=request.POST["no"]
    print("no="+no)
    password=request.POST["password"]
    models.deleteby_no_and_password(no,password)
    return HttpResponseRedirect("/guestbook01")