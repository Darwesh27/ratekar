(function() {
	angular.module('rateker.backend').
	service('Auth', [
		'$http', 
		'Me', 
		'$location',
		'$cookies',
		'$rootScope',
		'$mdDialog',
		'http',
		function($http, Me, $location, $cookies, $rootScope, $mdDialog, http){

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
				$http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];

				Me.sessionInit(username);

				loginStatus = true;

				return null;
			}

			this.signUpLogIn = function(user) {
				$http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
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

						// hide the login panel dialog
						$mdDialog.hide();

						// Initialize the me service to fetch user data
						Me.init(data.user);

						// User is logged in
						loginStatus = true;

						// Redirect to previous url or hoe

						if(Auth.beforeUrl != "/enter") {
							$location.path(Auth.beforeUrl);
						}
						else 
							$location.path("/");
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

					$rootScope.$broadcast('logOut');
					$rootScope.$emit('logOut');

				});
			};

			this.signUp = function(userData) {

				return http.post('/api/signup/', userData, '').then(
					function(data) {

						// hide the signup panel dialog
						$mdDialog.hide();

						Auth.signUpLogIn(data.user);

					},
					function(error) {

					}
				);

				$http.post('/api/signup/', userData).
				success(function(data) {
					if(!data.error) {

						// hide the signup panel dialog
						$mdDialog.hide();

						Auth.signUpLogIn(data);
					}
					else {
						cb(data.error);
					}
				});
			};
		}]);
})();