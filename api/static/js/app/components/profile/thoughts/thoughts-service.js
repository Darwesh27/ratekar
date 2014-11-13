(function() {
	angular.module('rateker.profile').
	service('Thoughts', [
		'$http',
		'Profile', 
		'$q', 
		'Urls'
		function($http, Profile, $q, Urls){

		var thoughts = {};
		var next = null;


		var general = function(method, url, serverError, cb) {
			var deffered = $q.defer();

			$http({method: method, url: url})
			success(function(data) {
				if(!data.error) {
					cb(data, deffered);
				}
				else {
					deffered.reject(data.error);
				}
			}).
			error(function(data) {
				deffered.reject(serverError);
			});

			return deffered.promise;

		}

		var getThoughts = function(url, error) {

			var callback = function(data , q) {

				// Store the next url in serivce
				next = data.next;

				// Tell the controller if it should ask for data or not..
				if(next != null) 
					data.next = true;
				else 
					data.next = false;

				q.resolve(data);
			})

			return general('get', url, error, callback);

		}
		
		this.get = function() {
			var url = Url.thoughts(Profile.username());
			var error = "Sorry we are unable to fetch Thoughts.. Please try again..";

			return getThoughts(url, error);

		}


		this.next = function() {
			var url = next;
			var error = "Sorry we are unable to fetch more Thoughts.. Please try again..";

			return getThoughts(url, error);
		}
	}]);
})();