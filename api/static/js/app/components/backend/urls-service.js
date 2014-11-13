(function() {
	angular.module('rateker.backend').
	service('Urls', ['Profile', function(Profile){

		var uPref = 'api/user/';
		
		this.thougts = function(username) {
			return uPref + username + '/thoughts';
		}
	}])
})();