from django.db          import models
from django.contrib     import admin
from django.utils       import timezone
from tinymce.models     import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=128)
    body = HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_edited = models.DateTimeField(auto_now=True)

class BlogAdmin(admin.ModelAdmin):
    pass
