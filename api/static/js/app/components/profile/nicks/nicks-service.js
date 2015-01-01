(function() {
	
	angular.module('rateker.profile').
	service('Nicks', [
		'ArrangeService',
		'Urls',
		function(ArrangeService, Urls){

			this.initUrl = function() {
				this.url = Urls.nicks(this.username);
				this.error = "Unable to Fetch Nicks";
			}

			ArrangeService.register(this);
		}]);
})();