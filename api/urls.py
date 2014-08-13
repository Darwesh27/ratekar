from django.conf.urls import patterns, url, include 
from api import views
from social import views as social_views
from personality import views as personality_views

user_patterns = patterns('',
		url(r'^circle/$', views.friendship_circle),
		url(r'^list/$', views.friendship_list),
		url(r'^rating/$', views.rating),
		url(r'^review/$', views.review),
		url(r'^feedback/(?<fbid>\d+)/$', views.feedback),
)


urlpatterns = patterns('',
		url(r'^friendship/$', views.friendship),
		url(r'^friendship/(?P<fid>\d+)/$', views.friendship_detail),
		url(r'^user/(?P<uid>\d+)/', include(user_patterns)),
		url(r'^friendslist/$', views.friendslist),
		url(r'^friendslist/(?<pk>\d+)/$', views.friendslist_detail),
)
