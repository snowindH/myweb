from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$',views.index,name='index'),
    url(r'^$',views.homepage),
    url(r'^post/(\w+)$',views.showpost),]
