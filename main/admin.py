from django.contrib import admin
from .models import Profile, Like, Comment, Photos

admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Photos)
