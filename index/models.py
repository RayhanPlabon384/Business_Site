from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=50,blank=False)
    description = models.TextField(max_length=500,blank=False)
    image = models.ImageField(upload_to='about/',blank=False)

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=50,blank=False)
    description = models.TextField(max_length=500,blank=False)
    image = models.ImageField(upload_to='slider/',blank=False)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=50,blank=False)
    link = models.TextField(max_length=500,blank=False)
    logo = models.ImageField(upload_to='client/',blank=False)

    def __str__(self):
        return self.name