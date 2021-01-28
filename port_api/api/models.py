from django.db import models

# Create your models here.

class homeModel(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500)
    def __str__(self):
        return self.name

