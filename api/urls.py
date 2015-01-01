from django.conf.urls import patterns, url, include 
from api import views
from social import views as social_views
from personality import views as personality_views

user_patterns = patterns('',
	#url(r'^feedback/(?<fbid>\d+)/$', views.feedback_details),
)

profile_patterns = patterns('',
	url(r'^circle/$', views.friendship_circle),
	url(r'^list/$', views.friendship_list),

	# url(r'^review/$', views.review),
	# url(r'^nick/$', views.nick),
	# url(r'^feedback/$', views.feedback),

	url(r'^profile/', views.profile),
	url(r'^thoughts/$', views.thoughts),
	url(r'^photos/$', views.photos),
	url(r'^feedbacks/$', views.feedbacks),
	url(r'^reviews/$', views.reviews),
	url(r'^nicks/$', views.nicks),
	url(r'^nick/$', views.nick),
	url(r'^feedback/$', views.feedback),
	url(r'^review/$', views.review),
	url(r'^reputation/$', views.reputation),
	url(r'^suggestnicks/$', views.suggest_nicks),
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

	url(r'^friendship/remove/$', views.unfriend),

	url(r'^friendship/requests/$', views.friend_requests),

	#url(r'^friendslist/(?<pk>\d+)/$', views.friendslist_details),


	# Liking a your reivew by someone
	url(r'^review/(?P<rid>\d+)/like$', views.like_review),

	###########################################################
	# Dialog related Urls
	###########################################################

	url(r'post/(?P<pid>\d+)/$', views.get_post),


	###########################################################
	# Toolbar related Urls
	###########################################################

	url(r'^search/$', views.search),

	###########################################################
	# Profile Urls
	###########################################################
	url(r'^friendship/status/(?P<username>[\w._-]+)/$', views.friendship_details),

	url(r'^feedbacks/new/$', views.new_feedback),

	###########################################################
	# Me related Urls
	###########################################################
	url(r'^me/thoughtsRating/$', views.my_thoughts_rating),


	###########################################################
	# Different Types of suggestions
	###########################################################

	# Friend Suggestions 
	url(r'^suggestions/friends/$', views.friend_suggestions),

	###########################################################
	# Privacy settings 
	###########################################################

	url(r'^post/privacy/$', views.post_privacy),



	###########################################################
	# Add a new Post 
	###########################################################


	# Post a status
	url(r'^post/status/$', views.post_status),

	# Rate a post
	url(r'post/(?P<pid>\d+)/rate/$', views.rate_post),


	# Comment on post 
	url(r'post/(?P<pid>\d+)/comment/$', views.add_comment),

	# Comments endpoint.. Fetching comments of a post
	url(r'^post/(?P<pid>\d+)/comments/$', views.comments),

	# Condemnn a comment
	url(r'^comment/(?P<cid>\d+)/condemn/$', views.condemn_comment),

	# Fetch the names of people who condemned this comment
	url(r'^comment/(?P<cid>\d+)/condemners/$', views.comment_condemners),

	# Post a photo 
	# url(r'post/photo/$', views.post_photo),


	###########################################################
	# Stream urls 
	###########################################################

	url(r'^stream/$', views.stream),
)
