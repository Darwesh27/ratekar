from django.conf.urls import patterns, url, include 
from api import views
from social import views as social_views
from personality import views as personality_views

user_patterns = patterns('',
	url(r'^circle/$', views.friendship_circle),
	url(r'^list/$', views.friendship_list),
	url(r'^reputation/$', views.reputation),
	url(r'^review/$', views.review),
	url(r'^nick/$', views.nick),
	url(r'^feedback/$', views.feedback),
	#url(r'^feedback/(?<fbid>\d+)/$', views.feedback_details),
)

profile_patterns = patterns('',
	url(r'^profile/', views.profile),
	url(r'^thoughts/$', views.thoughts),
	url(r'^photos/$', views.photos),
	url(r'^feedbacks/$', views.feedbacks),
	url(r'^reviews/$', views.reviews),
	url(r'^nicks/$', views.nicks),
	url(r'^mynick/$', views.my_nick),
	url(r'^myreview/$', views.my_review),
	url(r'^suggestnicks/$', views.suggest_nicks),
	url(r'^feedback/$', views.feedback),
)

urlpatterns = patterns('',
	url(r'^signup/$', views.signup),
	url(r'^login/$', views.signin),
	url(r'^logout/$', views.signout),
	url(r'^friendship/$', views.friendship),
	url(r'^friendship/(?P<fid>\d+)/$', views.friendship_details),
	url(r'^user/(?P<uid>\d+)/', include(user_patterns)),
	url(r'^user/(?P<username>\w+)/', include(profile_patterns)),
	url(r'^user/(?P<username>\w+)/check/$', views.profile),

	url(r'^friendslist/$', views.friendslist),
	#url(r'^friendslist/(?<pk>\d+)/$', views.friendslist_details),
	url(r'^review/(?P<rid>\d+)/like', views.like_review),
	url(r'^me/reviews/$', views.my_reviews),
	url(r'^me/feedbacks/$', views.my_feedbacks),
	url(r'^me/nicks/$', views.my_nicks),

	url(r'^post/(?P<pid>\d+)/comments/$', views.comments),


	url(r'^suggestions/friends/$', views.friend_suggestions),


)
