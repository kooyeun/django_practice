from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist02.models import Emaillist


def index():
    results=Emaillist.objects.all().order_by('-id')
    data = {"emaillist_list": results}
    return render(request, 'emaillist02/index.html', data)

def form(request):
    return render(request,'emaillist02/form.html')

def add(request):
    emaillist=Emaillist()
    emaillist.first_name=request.POST["fn"]
    emaillist.last_name=request.POST["ln"]
    emaillist.email=request.POST["email"]

    emaillist.save()


    return HttpResponseRedirect("/emaillist02")