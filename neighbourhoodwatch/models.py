from django.db import models
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="pictures")
    neighbourhood= models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    country = models.CharField(max_length=70)

class Post(models.Model):
    image = models.ImageField(default="default.jpg", upload_to="pictures")
    title = models.CharField(max_length=70)
    message = models.TextField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def show_posts(cls):
        return cls.objects.order("post_date")[::1]

class Neighbourhood(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    population = models.IntegerField()
    masterkey = models.ForeignKey(User, on_delete=models.CASCADE)

class Business(models.Model):
    name = models.CharField(max_length=25)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=250)
    
    @classmethod
    def search_businesses_by_title(cls,search):
        return cls.objects.filter(name__icontains=search)

