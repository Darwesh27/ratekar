(function() {
	angular.module('rateker.backend').
	service('Urls', [
		'Profile', 
		function(Profile){

			var Urls = this;

			var uPre = '/api/user/';


			var pre = function(username) {
				return uPre + username + "/";
			}
			
			this.get = function(resource) {

				return Profile.username().then(
					function(u){
						return pre(u) + resource + "/";
					}
				);
			}

			this.comments = function(postId) {
				return "api/post/" + postId + "/comments/";
			}

			this.nick = function() {
				return Urls.get('mynick');
			}

		}]);
})();