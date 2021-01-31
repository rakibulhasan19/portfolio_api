from django.db import models

# Create your models here.

class homeModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500)
    def __str__(self):
        return self.title
class aboutModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    about_me = models.TextField()
    name= models.CharField(max_length=100)
    dob=models.DateField()
    institute = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    cv = models.CharField(max_length=300)
    img_url = models.FileField()
    def __str__(self):
        return self.title



