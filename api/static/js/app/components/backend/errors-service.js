(function() {
	angular.module('rateker.backend').
	service('Errors', ['Profile', function(Profile){
		
		this.profileError = function(resource, next) {
			var more = (next == true)?"more ":"";
			return "Sorry we are unable to fetch " + more + resource;
		}


		this.friendSuggestions = function() {
			return "Some went wrong.. :P We are unable to fetch friend suggestions.. ";
		}



		/*
		 * New post related errors 
		 *
		 */

		this.postStatus = function() {
			return "Sorry..!! We are unable to post this status";
		}

		this.ratePost = function() {
			return "This post can't be rated right now..";
		}

		this.newComment = function() {
			return "Sorry..!! Unable to post comment.. Please try again later..";
		}

		this.condemnComment = function() {
			return "Sorry..!! Comment can't be condemned.. Please try again";
		}


		/*********************************
		* Stream realted errors 
		**********************************/

		this.stream = function() {
			return "Sorry..!! We are unable to fetch posts..";
		}



	}])
})();