from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses$', views.index, name='index'),
    url(r'^courses/add$', views.add, name='add'),
    url(r'^courses/destroy(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^courses/confirm(?P<id>\d+)$', views.confirm, name='confirm'),
]