from django.db import models

# Create your models here.

class contact(models.Model):
    sno =models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    content=models.TextField()
    email=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name