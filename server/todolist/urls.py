from django.conf.urls import url

from . import views
from django.conf.urls.static import static
from server import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list$', views.get_list, name='list'),
    url(r'^details/(?P<task_id>[0-9]+)$', views.details, name='list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
