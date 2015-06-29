from django.conf.urls import patterns, url, include
from features import views

# the name value is called by the url template tag
urlpatterns = patterns('',
    # ex: /features/
    url(r'^$', views.index, name='index'),
    # ex: /features/5/
    url(r'^(?P<feature_id>\d+)/$', views.detail, name='detail'),
    # ex: /features/new-feature/
    url(r'^new-feature$', views.create_feature, name='new-feature'),
    url(r'^edit/(?P<feature_id>\d+)/$', views.create_feature, name='new-feature'),
    url(r'^search/', include('haystack.urls')),
    # url(r'^search/$', views.search, name='search'),
)
