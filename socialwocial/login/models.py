from django.db import models

# Create your models here.
class users(models.Model):
    realname = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    phone = models.PositiveBigIntegerField()
    profilepic = models.ImageField(upload_to='profileimages')
    emailid = models.EmailField(max_length=254)
    quailification = models.CharField(max_length=200)
    dob = models.DateField()
    idname = models.CharField(max_length=20)
    banner_image = models.ImageField(upload_to='bannerImages')
    timeofjoin = models.DateField(auto_now_add=True)
    
