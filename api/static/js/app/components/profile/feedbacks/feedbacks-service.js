(function() {
	angular.module('rateker.profile').
	service('Feedbacks', [
		'ArrangeService',
		'Urls',
		function(ArrangeService, Urls){

			this.initUrl = function() {
				this.url = Urls.feedbacks(this.username);
				this.error = "Unable to Fetch Feedbacks";
			}

			ArrangeService.register(this);
		}]);
})();