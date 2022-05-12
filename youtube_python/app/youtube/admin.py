from xml.etree.ElementTree import Comment
from django.contrib import admin
from django import *

from app.youtube.models import Channel, Channel_Subscription,Comment, Dislike, Like, Video, Video_View
# Register your models here.
admin.site.register([Video,Comment,Channel,Like,Dislike,Video_View, Channel_Subscription]) 