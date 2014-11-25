(function() {
	angular.module('rateker.profile').
	service('Feedback', [
		'$http',
		'Profile', 
		'Fetch',
		'Urls',
		'Errors',
		function($http, Profile, Fetch, Urls, Errors){

			this.get = function() {
				return Urls.get('feedback').then(
					function(url){
						var error = "Something went wrong in here.. ";
						return Fetch.fetch(url, error, function(data, q) {
							q.resolve(data);
						});
					}
				);
			}

			this.give = function(feedback) {

				return Urls.get('feedback').then(
					function(url){
						var data = {
							feedback: feedback,
						}
						var error = "Something went wrong here ";
						return Fetch.http('post', url, data, error, function(data, q) {
							q.resolve(data);
						})
					}
				);
			}

			this.skip = function(feedback) {
				return Urls.get('feedback').then(
					function(url){
						var data = {
							feedback: feedback,
							skip: true,
						}
						var error = "Something went wrong here ";
						return Fetch.http('post', url, data, error, function(data, q) {
							q.resolve(data);
						})
					}
				);

			}
		}]);
})();