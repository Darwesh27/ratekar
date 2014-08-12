from django.conf.urls import patterns, url


urlpatterns = patterns('',
		url(r'^friendship/$', views.friendship),
		url(r'^friendship/(?<fid>[0-9]+)/$', views.friendship_detail),
		url(r'^friendship/(?<fid>[0-9]+)/circle/$', views.friendship_circle),
		url(r'^friendship/(?<fid>[0-9]+)/list/$', views.friendship_list),

