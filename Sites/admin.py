from django.contrib import admin
from Sites import models

admin.site.register(models.Site, models.SiteAdmin)
