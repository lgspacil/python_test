from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^login$', views.login),
  url(r'^register$', views.register),
  url(r'^success$', views.success),
  url(r'^create_item_page/(?P<id>\d+)$', views.create_item_page),
  url(r'^add_item$', views.add_item),
  url(r'^delete_item/(?P<id>\d+)$', views.delete_item),
  url(r'^add_your_list/(?P<id>\d+)$', views.add_your_list),
  url(r'^remove_wish_list/(?P<id>\d+)$', views.remove_wish_list),
  url(r'^item_detail/(?P<id>\d+)$', views.item_detail),

   

  ]