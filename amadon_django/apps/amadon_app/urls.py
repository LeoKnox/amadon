from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^purchase$', views.purchase),
    url(r'^purchase_redirect$', views.purchase_redirect),
]