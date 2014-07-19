from django.conf.urls import patterns, url
from game import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /play/5/
    url(r'^(?P<scene_id>\d+)/$', views.scene, name='scene'),
    # ex: /play/option/5
    url(r'^option/(?P<option_id>\d+)$', views.option, name='option'),
)
