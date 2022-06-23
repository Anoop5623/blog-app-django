from distutils.command.upload import upload
from tkinter import CASCADE
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
from matplotlib import image
from matplotlib.pyplot import title
from froala_editor.fields import FroalaField
from tinymce.models import HTMLField
from .helper import *
from django.utils.timezone import now

# Create your models here.
class blogmodel(models.Model):
    title=models.CharField(max_length=1000)
    content=HTMLField()
    slug=models.SlugField(max_length=1000, null=True, blank=True)
    author=models.CharField(max_length=30)
    image=models.ImageField(upload_to='blogimg/')
    created_at=models.DateTimeField(auto_now_add=True)
    upload_to= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug=generate_slug(self.title)
        super(blogmodel,self).save(*args,**kwargs)    



class blogcomment(models.Model):
    sno=models.AutoField(primary_key=True)
    comments=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(blogmodel,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comments[:15]+ '... by ' + self.user.username

            


