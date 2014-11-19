(function() {
	angular.module('rateker.profile').
	service('Review', [
		'$http',
		'Profile', 
		'Urls', 
		'Fetch',
		function($http, Profile, Urls, Fetch){

			this.get = function() {
				return Urls.get('myreview').then(
					function(url){
						var error = "Unable to fetch the Review.. ";
						return Fetch.fetch(url, error, function(data, q) {
							q.resolve(data);
						});
					}
				);
			}

			this.give = function(review) {

				return Urls.get('myreview').then(
					function(url){
						data = {
							review : review,
						}
						var error = "Unable to update the Review.. ";
						return Fetch.http('post', url, data, error, function(data, q) {
							q.resolve(data);
						})
					}
				);
			}
		
	}]);
})();