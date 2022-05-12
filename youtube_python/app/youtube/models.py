from time import timezone
from django.db import models

# Create your models here.
class Video (models.Model):
    title = models.CharField(max_length=30)
    desciption=models.TextField(max_length=300)
    path=models.CharField(max_length=60)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False) #todo: auto_now=True
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Channel(models.Model):
    channel_name = models.CharField(max_length=50, blank=False, null=False)
    subscribers = models.IntegerField(default=0, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Dislike(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Video_View(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

class Channel_Subscription(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)