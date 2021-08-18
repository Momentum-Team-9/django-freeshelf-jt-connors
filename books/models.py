from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField, URLField

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Category", related_name="books", null=True, blank=True)
    
    def __str__(self):
        return f'{self.title}, {self.author}'

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f'{self.name}'
