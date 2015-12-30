from django.db import models
from django.contrib import admin

class Site(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, null=True)
    link = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    thumbnail_filename = models.CharField(max_length=128)

class SiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'subtitle')
