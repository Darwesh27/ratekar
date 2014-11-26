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

	##########################################################
	# Authentication
	##########################################################

	# The names suggest
	url(r'^signup/$', views.signup),
	url(r'^login/$', views.signin),
	url(r'^logout/$', views.signout),

	# Checking the availibility of username and email
	url(r'^signup/check/username/$', views.check_username),
	url(r'^signup/check/email/$', views.check_email),


	# User data 
	url(r'^user/(?P<username>[\w._-]+)/', include(profile_patterns)),


	# Social services like adding people to list and things
	url(r'^user/(?P<uid>\d+)/', include(user_patterns)),
	url(r'^friendslist/$', views.friendslist),

	# Friend Request sending and approval 
	url(r'^friendship/$', views.friendship),
	url(r'^friendship/(?P<fid>\d+)/$', views.friendship_details),

	#url(r'^friendslist/(?<pk>\d+)/$', views.friendslist_details),


	# Liking a your reivew by someone
	url(r'^review/(?P<rid>\d+)/like', views.like_review),


	# This is chuss
	url(r'^me/reviews/$', views.my_reviews),
	url(r'^me/feedbacks/$', views.my_feedbacks),
	url(r'^me/nicks/$', views.my_nicks),


	# Comments endpoint.. Fetching comments of a post
	url(r'^post/(?P<pid>\d+)/comments/$', views.comments),


	###########################################################
	# Different Types of suggestions
	###########################################################

	# Friend Suggestions 
	url(r'^suggestions/friends/$', views.friend_suggestions),


	###########################################################


)
