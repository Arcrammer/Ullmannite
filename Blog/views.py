from . import models
from django.shortcuts import render

def all(request):
    view_data = {
        'posts': models.Blog.objects.all()
    }
    return render(request, 'all-posts.html', view_data)
