from django.conf.urls import patterns, include, url
from api import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ratekar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include('api.urls', namespace = 'api')),
	url(r'^.*$', views.index),
)
