(function() {
	
	angular.module('rateker.profile').
	service('Nicks', [
		'Fetch',
		function(Fetch){

			this.next = null;

			var Nicks = this;
		
			this.get = function() {
				return Fetch.get(Nicks, 'nicks');
			}


			this.next = function() {
				return Fetch.next(Nicks, 'nicks');
			}
		}]);
})();