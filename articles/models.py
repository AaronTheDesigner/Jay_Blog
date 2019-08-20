from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    #slug = models.SlugField(max_length=50, allow_unicode=True, unique=True)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default="default.jpg", upload_to="article_pics" )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        return f'(self.user.username) Image'

class Cover(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    description = models.TextField()
    author = models.TextField()
    blogger = models.TextField()
    link_1 = models.URLField()

class Novel(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField()
    blurb = models.TextField()
    link = models.URLField()
        
class Novella(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField()
    blurb = models.TextField()
    link = models.URLField()
        
class Short(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField()
    blurb = models.TextField()
    link = models.URLField()

class Event(models.Model):
    event = models.CharField(max_length=50)
    event_picture = models.ImageField()
    description = models.TextField(max_length=500)
    link = models.URLField()

class Feature(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField()
    blurb = models.TextField()
        

