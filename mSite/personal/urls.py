from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ability/$', views.ability, name='ability'),
    url(r'^contact/$', views.contact, name='contact'),
]
