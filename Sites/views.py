from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from Sites import models

@require_GET
def all(request):
    sites = models.Site.objects.all()
    last_site_is_loner = (models.Site.objects.count() % 2 != 0)
    view_data = {
        'last_site_is_loner': last_site_is_loner,
        'sites': sites
    }
    return render(request, 'all.html', view_data)
