from django.shortcuts import render,HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.
def getcontact(request):
    if request.method=='POST':
        namee=request.POST['name']
        phonenoo=request.POST['phoneno']
        contentt=request.POST['content']
        emaill=request.POST['email']
        #print(name,phoneno,content,email)
        en=contact(name=namee, phone=phonenoo, email=emaill, content=contentt)
        en.save()
        messages.success(request,' : query sent successfully ')
    return render(request,'contact.html')
    #return HttpResponse("hello")
    