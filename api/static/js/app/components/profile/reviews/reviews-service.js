(function() {
	
	angular.module('rateker.profile').
	service('Reviews', [
		'Urls',
		'Errors',
		'ArrangeService',
		function(Urls, Errors, ArrangeService){

			this.initUrl = function() {
				this.url = Urls.reviews(this.username);
				this.error = "Unable to Fetch Reviews";
			}

			ArrangeService.register(this);
		}]);
})();