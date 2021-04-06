from django.http import HttpResponseRedirect
from django.shortcuts import render


from guestbook02.models import Guestbook


def index(request):
    results=Guestbook.objects.all().order_by('-regdate')
    guestList={'guest_list': results}
    return render(request,'guestbook02/index.html',guestList)

def guestAdd(request):
    guestbook=Guestbook()
    guestbook.name=request.POST["name"]
    guestbook.password=request.POST["password"]
    guestbook.message=request.POST["message"]

    guestbook.save()

    return HttpResponseRedirect("/guestbook02")

def deleteForm(request):
#    id=request.GET["id"]
#    num={'id':id}
#    return render(request,"guestbook02/deleteform.html",num)
    return render(request,"guestbook02/deleteform.html")

def guestDelete(request):

    #id=request.POST["id"]

    #password=request.POST["password"]
    #models.deleteby_no_and_password(no,password)
    guestbook=Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['password'])
    guestbook.delete()
    return HttpResponseRedirect("/guestbook02")