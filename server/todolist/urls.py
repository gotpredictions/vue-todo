from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list$', views.get_list, name='list'),
    url(r'^details/(?P<task_id>[0-9]+)$', views.details, name='list'),
]
