from django.db import models
from django.conf import settings
from django.contrib import admin

class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title

admin.site.register(Blogpost)