(function() {
	angular.module('rateker.backend').
	service('Urls', [
		'Profile', 
		function(Profile){

			var Urls = this;

			var uPre = '/api/user/';

			var api = function() {

				return "/api/";

			}


			var pre = function(username) {
				return uPre + username + "/";
			}

			var userUrl = function(username) {
				return api() + "user/" + username + "/";
			}
			
			this.get = function(resource) {

				return Profile.username().then(
					function(u){
						return pre(u) + resource + "/";
					}
				);
			}



			/************************************************
			* Welcome Urls
			************************************************/

			this.suggestPlaces = function() {
				return api() + "/suggestions/places/";
			}

			this.updatePlaces = function() {
				return api() + "update/places/";
			}


			/************************************************
			* Dialog Urls
			************************************************/

			this.getPost = function(postId) {
				return api() + 'post/' + postId + "/";
			}

			this.getReview = function(reviewId) {
				return api() + 'review/' + reviewId + "/";
			}

			/************************************************
			* Toolbar Urls
			************************************************/

			this.search = function(input) {
				return api() + "search/" + "?q=" + input;
			}

			this.friendRequests = function() {
				return api() + "friendship/requests/";
			}

			/************************************************
			* Friendship related Urls
			************************************************/

			this.addFriend = function() {
				return api() + "friendship/";
			}

			this.friendStatus = function(username) {
				return api() + "friendship/status/" + username + "/";
			}

			this.changeCircle = function(username) {
				return api() + "user/" + username + "/circle/";
			}

			this.unfriend = function() {
				return api() + 'friendship/remove/'; 
			}

			/************************************************
			* Profile Urls
			************************************************/


			this.thoughts = function(username) {
				return api() + "user/" + username + "/thoughts/";
			}

			this.reviews = function(username) {
				return api() + "user/" + username + "/reviews/";
			}

			this.nicks = function(username) {
				return api() + "user/" + username + "/nicks/";
			}

			this.feedbacks = function(username) {
				return api() + "user/" + username + "/feedbacks/";
			}


			this.newFeedback = function() {
				return api() + "feedbacks/new/";
			}

			this.suggestNicks = function(username) {
				return userUrl(username) + "suggestnicks/";
			}

			this.rankings = function() {
				return api() + 'rankings/';
			}

			/************************************************
			* Me related urls 
			************************************************/

			this.myThoughtsRating = function() {
				return api() + "me/thoughtsRating/";
			}

			this.nick = function() {
				return Urls.get('nick');
			}

			this.friendSuggestions = function() {
				return api() + 'suggestions/friends/';
			}

			this.checkUsername = function() {
				return api() + 'signup/check/username/';
			}

			this.checkEmail = function() {
				return api() + 'signup/check/email/';
			}


			/************************************************
			* Post related urls 
			************************************************/

			this.postStatus = function() {
				return api() + "post/status/";
			}

			this.ratePost = function(postId) {
				return api() + "post/" + postId + "/rate/";
			}

			this.newComment = function(postId) {
				return api() + "post/" + postId + "/comment/";
			}

			this.comments = function(postId) {
				return api() + "post/" + postId + "/comments/";
			}

			this.nextComments = function(postId, next, befNext) {
				if(next != null)
					return Urls.comments(postId) + "?nFTime=" + next + "&befNext=" + befNext;
				else 
					return Urls.comments(postId);
			}

			this.previousComments = function(postId, previous, befPrev) {
				return Urls.comments(postId) + "?pFTime=" + previous + "&befPrev=" + befPrev;
			}

			this.condemnComment = function(commentId) {
				return api() + "comment/" + commentId + "/condemn/";
			}

			this.commentCondemners = function(commentId) {
				return api() + "comment/" + commentId + "/condemners/";
			}

			/************************************************
			* Stream related urls 
			************************************************/

			this.stream = function() {
				return api() + "stream/";
			}

			this.streamNextPosts = function(time, id) {
				if(time != null) 
					return  Urls.stream() + "?nFTime=" + time + "&nextId=" + id;
				else 
					return Urls.stream();
			}

			this.streamPreviousPosts = function(time, id) {
				return  Urls.stream() + "?pFTime=" + time + "&prevId=" + id;
			}

		}]);
})();