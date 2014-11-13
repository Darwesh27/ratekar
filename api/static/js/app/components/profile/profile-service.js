(function() {
	angular.module('rateker.profile').
	service('Profile', [
		'$http', 
		'Auth', 
		'$q',
		'$timeout',
		function($http, Auth, $q, $timeout){
		
		var Profile = this;

		this.profile = null;


		this.check = function() {

			console.log("Hello");
			var deffered = $q.defer();

			$timeout(function() {
				deffered.resolve("Hello");
			}, 1000);

			return deffered.promise;
		}

		this.init = function(username) {

			// First delete the preivous profile
			this.profile = null;


			var defer = $q.defer();

			// get data from server 
			$http.get('api/user/' + username + '/profile/', {username: username}).
			success(function(data) {
				if(!data.error) {
					Profile.profile = data;

					defer.resolve(data);
				}
				else {
					defer.reject(data);
				}
			});

			return defer.promise;
		}
	}]);
})();