from django.conf.urls import url
from Sites import views

urlpatterns = [
    url(r'^$', views.all),
]
