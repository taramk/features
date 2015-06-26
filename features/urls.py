from django.conf.urls import patterns, url
from features import views

# the name value is called by the url template tag
urlpatterns = patterns('',
    # ex: /requests/
    url(r'^$', views.index, name='index'),
    # ex: /requests/5/
    url(r'^(?P<feature_id>\d+)/$', views.detail, name='detail'),
    # ex: /requests/5/results/
    url(r'^new-feature$', views.create_feature, name='new-feature'),
    url(r'^edit/(?P<feature_id>\d+)/$', views.create_feature, name='new-feature')
)
