from django.db import models
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("=========================================[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]=")

    if created:
        Profile.objects.create(user=instance)
        print("==========================================")


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="pictures")
    bio = models.CharField(max_length=250, null=True)
    age = models.IntegerField(null=True)
    neighbourhood =  models.CharField(max_length=30, null=True)

class Post(models.Model):
    image = models.ImageField(default="default.jpg", upload_to="pictures")
    title = models.CharField(max_length=70)
    message = models.TextField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    masterpost = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
    def get_absolute_url(self):
        return reverse('index')
    
    @classmethod
    def show_posts(cls):
        return cls.objects.order("post_date")[::1]

class Neighbourhood(models.Model):
    name = models.CharField(max_length=25)
    population = models.IntegerField()
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default="default.jpg", upload_to="pictures")
    post_date = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('neighbourhood-detail', kwargs={'pk':self.pk})
        

    @classmethod
    def show_businesses(cls):
        return cls.objects.order_by("post_date")[::1]

class Business(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=250)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    
    @classmethod
    def search_businesses_by_name(cls,search):
        return cls.objects.filter(name__icontains=search)