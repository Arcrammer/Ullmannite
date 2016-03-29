from django.contrib import admin
from Blog import models

admin.site.register(models.Blog, models.BlogAdmin)
