from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^test/$', views.posts_page), # test
    url(r'^$', views.all),  # get list
    url(r'^create/$', views.create),  # get detail
    url(r'^detail/$', views.detail),  # get detail
    url(r'^delete/$', views.delete),  # detele
    url(r'^update/$', views.update), # update
]