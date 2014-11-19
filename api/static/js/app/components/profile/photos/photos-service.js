(function() {

	angular.module('rateker.profile').
	service('Photos', [
		'Fetch',
		function(Fetch){

			this.next = null;

			var Photos = this;
		
			this.get = function() {
				return Fetch.get(Photos, 'photos');
			}


			this.next = function() {
				return Fetch.next(Photos, 'photos');
			}
		}]);
})();