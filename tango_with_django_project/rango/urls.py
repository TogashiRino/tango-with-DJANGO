from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register,
        name='register'),


]
