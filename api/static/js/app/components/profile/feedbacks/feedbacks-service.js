(function() {
	angular.module('rateker.profile').
	service('Feedbacks', [
		'Fetch',
		function(Fetch){

			this.next = null;

			var Feedbacks = this;

			this.get = function() {
				return Fetch.get(Feedbacks, 'feedbacks');
			}


			this.next = function() {
				return Fetch.next(Feedbacks, 'feedbacks');
			}
		}]);
})();