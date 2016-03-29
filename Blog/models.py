from django.db          import models
from django.contrib     import admin
from django.utils       import timezone
from tinymce.models     import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=128)
    body = HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_edited = models.DateTimeField(null=True, auto_now_add=True)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'last_edited')
