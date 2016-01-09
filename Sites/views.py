from django.shortcuts import render
from django.http import HttpResponse
from Sites import models

def all(request):
    sites = models.Site.objects.all()
    last_site_is_loner = (models.Site.objects.count() % 2 != 0)
    view_data = {
        'last_site_is_loner': last_site_is_loner,
        'sites': sites
    }
    return render(request, 'all.html', view_data)
