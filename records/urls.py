from django.conf.urls import url
from . import views

app_name = 'records'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'add/$', views.PatientCreate.as_view(), name='patient-add'),
    url(r'(?P<pk>[0-9]+)/update/$', views.PatientUpdate.as_view(), name='patient-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', views.PatientDelete.as_view(), name='patient-delete'),
]
