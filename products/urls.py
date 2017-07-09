from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.categories, name='categories'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.product_delete, name='product_delete'),
     url(r'^success$', views.success, name='success'),

    
    
]
