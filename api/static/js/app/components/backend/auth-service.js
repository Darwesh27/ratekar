(function() {
	angular.module('rateker.backend').
	service('Auth', ['$http', function($http){
		var loginStatus = true;

		this.isLoggedIn = function() {
			return loginStatus;
		};
	}]);
})();