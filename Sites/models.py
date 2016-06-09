from django.db import models
from django.contrib import admin

class Site(models.Model):
    class Meta:
        db_table = 'sites'
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, null=True)
    link = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    thumbnail_filename = models.CharField(max_length=128)
    precedence = models.FloatField(max_length=128, default=0)

class SiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'subtitle', 'precedence')
