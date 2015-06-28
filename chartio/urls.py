from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^features/', include('features.urls', namespace="features")),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'', include('django_browserid.urls'))
)
