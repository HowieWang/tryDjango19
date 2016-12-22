from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^test/$', views.posts_page), # test
    url(r'^$', views.all, name='list'),  # get list
    url(r'^create/$', views.create),  # get detail

    # url(r'^detail/$', views.detail),  # get detail
    # url(r'^detail/(?P<id>\d+)/$', views.detail),  # get detail
    # url(r'^(?P<id>\d+)/$', views.detail),  # get detail
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),  # get detail, add name=
    
    url(r'^(?P<id>\d+)/delete/$', views.delete),  # detele
    url(r'^(?P<id>\d+)/edit/$', views.update, name='update'),  # update
] 