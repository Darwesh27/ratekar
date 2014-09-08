from django.contrib import admin
from social.models import User, Friendslist, Friendship
from personality.models import Reputation, Review, TraityQuestion, Feedback

class ReputationAdmin(admin.ModelAdmin):
	pass

class ReviewAdmin(admin.ModelAdmin):
	pass

class TraityQuestionAdmin(admin.ModelAdmin):
	pass

class FeedbackAdmin(admin.ModelAdmin):
	pass

class UserAdmin(admin.ModelAdmin):
	pass

class FriendshipAdmin(admin.ModelAdmin):
	pass

class FriendslistAdmin(admin.ModelAdmin):
	pass

admin.site.register(User)
admin.site.register(Friendship, FriendshipAdmin)
admin.site.register(FriendslistAdmin, FriendslistAdmin)
admin.site.register(Reputation, ReputationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(TraityQuestion, TraityQuestionAdmin)
admin.site.register(Feedback, FeedbackAdmin)
