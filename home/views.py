import profile
from urllib import request
from django.shortcuts import render,HttpResponse,redirect
from .models import blogmodel, blogcomment
from django.contrib.auth.models import User
from django.contrib import messages
from home.templatetags import extras
from django.contrib.auth import authenticate, login, logout 

# Create your views here.
def home(request):
   if request.method=="POST":
      search=request.POST.get('search')
      post =blogmodel.objects.filter(title__icontains=search)
      return render(request, 'home.html',{'blog': post})
   else:
      post =blogmodel.objects.all()
      return render(request, 'home.html',{'blog': post}) 
   

def blogdescription(request,string):
   post=blogmodel.objects.get(slug=string)
   comments=blogcomment.objects.filter(post=post,parent=None)
   replies=blogcomment.objects.filter(post=post).exclude(parent=None)
   replydict={}
   for reply in replies:
      if reply.parent.sno not in replydict.keys():
         replydict[reply.parent.sno]=[reply]
      else:
         replydict[reply.parent.sno].append(reply) 
   data={'post': post,'comments':comments, 'user':request.user,'replydict': replydict}
   return render(request,'blogdesc.html',data)


def createblog(request):
   if request.method=="POST":
      title=request.POST.get('title')
      author=request.POST.get('author')
      content=request.POST.get('content')
      image=request.FILES['image']
      print(title,author,content,image)
      ev=blogmodel(title=title,author=author,content=content,image=image)
      ev.save()
      messages.success(request,' : posted blog')
      return redirect("/")
   return render(request,'blog.html')




def postcomment(request):
   if request.method=='POST':
      comment=request.POST['comment']
      user=request.user
      postsno=request.POST.get('postsno')
      commentno=request.POST.get('commentno') 
      post=blogmodel.objects.get(id=postsno)
      if commentno=="":
         comment=blogcomment(comments=comment,user=user,post=post)
         comment.save()
         messages.success(request,' : posted comment')
      else:
         parent=blogcomment.objects.get(sno=commentno)
         print(comment,user,post,parent)
         comment=blogcomment(comments=comment,user=user,post=post,parent=parent)
         comment.save()
         messages.success(request,' : posted reply')
   return redirect(f'/blog/{post.slug}')
   
   


def signup(request):
   if request.method=='POST':
      username=request.POST['username']
      name=request.POST['name']
      email=request.POST['email']   
      pass1=request.POST['password1']
      pass2=request.POST['password2']
      #print(username,name,email,pass1,pass2)
      if len(username)<10:
         messages.error(request," username mustbe greater than 10 characters")
         return render(request,'signup.html')
      if not username.isalnum():
         messages.error(request," username mustbe be alphanumeric")  
         return render(request,'signup.html')
      if pass1 != pass2:
         messages.error(request," passwords not matching")
         return render(request,'signup.html')
         
      elif len(username)>10 and username.isalnum() and pass1 == pass2: 
         myuser=User.objects.create_user(username,email,pass1)
         myuser.first_name=name
         myuser.save()
         messages.success(request,' : user successfully created')
         return redirect('/login')
   return render(request,'signup.html')

def handlelogin(request):
   if request.method=='POST':
      username=request.POST['username']
      pass3=request.POST['password']  
      #print(username,pass3) 
      user=authenticate(username=username,password=pass3)
      if user is not None:
         login(request,user)
         messages.success(request, username+" successfully loged in ")
         return redirect("/")
      else:
         messages.error(request,"invalid credentials")
         return render(request,'login.html')   
   return render(request,'login.html')      

def handlelogout(request):
   logout(request)
   messages.success(request," successfully loged out ")
   return redirect('/')  