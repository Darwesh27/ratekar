(function() {
	angular.module('rateker.profile').
	service('Profile', [
		'$http', 
		'$q',
		'$timeout',
		'http',
		function($http, $q, $timeout, http){
		
		var Profile = this;

		this.profile = null;


		this.ready = function() {
			var deffered = $q.defer();

			$timeout(function(){
				while(Profile.profile == null){
				}

				deffered.resolve(true);
			},500);

			return deffered.promise;
		}


		this.username = function() {
			var deffered = $q.defer();

			Profile.ready().
			then(function() {
				deffered.resolve(Profile.profile.username);
			});

			return deffered.promise;
		}


		this.check = function() {

			var deffered = $q.defer();

			$timeout(function() {
				deffered.resolve("Hello");
			}, 1000);

			return deffered.promise;
		}

		this.init = function(username) {

			// First delete the preivous profile
			Profile.profile = null;


			var defer = $q.defer();

			// get data from server 
			$http.get('api/user/' + username + '/profile/', {username: username}).
			success(function(data) {

				Profile.profile = data;

				defer.resolve(data);

				// if(!data.error) {
				// 	Profile.profile = data;

				// 	defer.resolve(data);
				// }
				// else {

				// 	console.log("Rejecting Data");
				// 	defer.reject(data.error);
				// }
			});

			return defer.promise;
		}


		this.rate = function(profile, rating) {

			var url = "/api/user/" + profile.username + "/reputation/";
			var error = "Error while giving reputation";

			http.post(url, {reputation: rating}, error).then(
				function(data) {
					profile.reputation = data.reputation;
				},
				function(error) {
					//TODO 
				}
			);

		}

	}]);
})();