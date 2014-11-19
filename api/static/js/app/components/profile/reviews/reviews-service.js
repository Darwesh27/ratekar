(function() {
	
	angular.module('rateker.profile').
	service('Reviews', [
		'Fetch',
		function(Fetch){

			this.next = null;

			var Reviews = this;
		
			this.get = function() {
				return Fetch.get(Reviews, 'reviews');
			}


			this.next = function() {
				return Fetch.next(Reviews, 'reviews');
			}
		}]);
})();