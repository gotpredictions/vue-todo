from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list$', views.get_list, name='list'),
    url(r'^create$', views.create, name='create'),
    url(r'^details/(?P<task_id>[0-9]+)$', views.details, name='details'),
    url(r'^update/(?P<task_id>[0-9]+)$', views.update, name='update'),
]
