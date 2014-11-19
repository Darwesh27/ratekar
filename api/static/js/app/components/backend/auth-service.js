(function() {
	angular.module('rateker.backend').
	service('Auth', [
		'$http', 
		'Me', 
		'$location',
		function($http, Me, $location){

			var Auth = this;

			this.beforeUrl = "/";

			var loginStatus = false;

			this.toggleStatus = function() {
				loginStatus = !loginStatus;
			};

			this.isLoggedIn = function() {
				return loginStatus;
			};

			this.sessionLogIn = function(username) {
				Me.sessionInit(username);

				loginStatus = true;

				return null;
			}

			this.signUpLogIn = function(user) {
				Me.init(user);

				loginStatus = true;
			}

			this.logIn = function(credential, password, cb) {
				var data  = {
					username: credential,
					password: password,
				}

				$http.post("/api/login/", data).
				success(function(data, status, headers, config){
					if(!data.error) {

						// Initialize the me service to fetch user data
						Me.init(data.user);

						// User is logged in
						loginStatus = true;

						// Redirect to previous url or hoe
						console.log(Auth.beforeUrl);
						$location.path(Auth.beforeUrl);
					}
					else {
						cb(data.error);
					}
				}).
				error(function(data, status, headers, config) {
					cb("Sorry..!! We encountered an internal problem.. Please try again.. :)");
				})
			};

			this.logOut = function() {
				$http.get("/api/logout/").
				success(function(data, status, headers, config) {
					Me.destroy();

					loginStatus = false;

				});
			};

			this.signUp = function(userData, cb) {
				$http.post('/api/signup/', userData).
				success(function(data) {
					if(!data.error) {
						Auth.signUpLogIn(data);
					}
					else {
						cb(data.error);
					}
				});
			};
		}]);
})();