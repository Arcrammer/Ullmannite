from django.shortcuts import render
from django.http import HttpResponse
from Sites import models

def all(request):
    view_data = {
        'sites': models.Site.objects.all()
    }
    return render(request, 'all.html', view_data)
