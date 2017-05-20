from django.db import models
from django.contrib import admin

class Site(models.Model):
    class Meta:
        db_table = 'sites'
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=128)
    link = models.CharField(max_length=128)
    thumbnail_filename = models.CharField(max_length=128)
    online = models.BooleanField(default=False)

class SiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'subtitle')
