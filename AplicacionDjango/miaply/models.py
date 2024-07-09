from django.db import models

# Create your models here.

class Article(models.Model):
    title= models.CharField(max_length=100)
    content= models.TextField()
    image=models.ImageField(default='')
    public= models.BooleanField()
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)


class category(models.Model):    
    name= models.CharField(max_length=110)
    description= models.CharField(max_length=250)
    created_at= models.DateField()