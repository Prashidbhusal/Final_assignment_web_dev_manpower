from django.db import models

from django.contrib.auth.models import User





class Profile(models.Model):
    user= models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    username=models.CharField(max_length=200,null=True)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic=models.FileField(upload_to='static/uploads',
                                 default='static/images/figma.jpg')
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
