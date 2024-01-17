from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.title

class Form(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField(default = 'example@gmail.com')
    is_checked = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['is_checked', '-created']
    