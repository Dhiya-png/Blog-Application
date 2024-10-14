from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

# for uploading post

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    media = models.ImageField(upload_to='media/',null=True,blank=True)
    content = RichTextField()
    tags = models.CharField(max_length=50,blank=True,null=True)

# for post management

class PostModel(models.Model):
    title = models.CharField(max_length=30)
    content = RichTextField()
    tags = models.CharField(max_length=100)

    