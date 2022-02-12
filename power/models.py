from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class Vacancy (models.Model):
    title=models.CharField(max_length=200, null=True)
    salary= models.IntegerField(default=0)
    totalVacancy= models.IntegerField(default=0)
    features = models.CharField(max_length=1000)

    def __str__(self):
        return self.title



class VacancyForm (models.Model):
    vacancy= models.ForeignKey(Vacancy, null=True, on_delete=models.CASCADE)
    user= models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='suser')
    name= models.CharField(max_length=100, null=True)
    dob= models.CharField(max_length=20, null=True)
    cv= models.FileField(upload_to='static/useruploads', null=True)
    citizenship = models.ImageField(upload_to='static/usercitizen', null=True)
    qualification = models.CharField(max_length=1000)
    applied =  models.BooleanField(default=False)
    seen= models.BooleanField(default=False)
    response= models.CharField(max_length=1000, null=True)


    def __str__(self):
        return self.name

    @property
    def filename(self):
        return os.path.basename(self.cv.name)
    
     

class Message(models.Model):
    name= models.CharField(max_length=100, null=True)
    email= models.EmailField(null=True)
    query= models.CharField(max_length=1000, null=True)
    response= models.CharField(max_length=1000)
    date =models.DateField(auto_now_add=True, null=True)
    seen = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    