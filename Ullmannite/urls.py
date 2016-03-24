from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # CMS
    url(r'^admin', admin.site.urls),

    # Sites
    url(r'^', include('Sites.urls')),
]
