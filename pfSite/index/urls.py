from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^ability/$', views.ability, name='ability'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^contact/$', views.contact, name='contact'),
]
