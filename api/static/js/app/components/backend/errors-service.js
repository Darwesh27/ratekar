(function() {
	angular.module('rateker.backend').
	service('Errors', ['Profile', function(Profile){
		
		this.profileError = function(resource, next) {
			var more = (next == true)?"more ":"";
			return "Sorry we are unable to fetch " + more + resource;
		}


		this.friendSuggestions = function() {
			return "Some went wrong.. :P We are unable to fetch friend suggestions.. ";
		}

	}])
})();