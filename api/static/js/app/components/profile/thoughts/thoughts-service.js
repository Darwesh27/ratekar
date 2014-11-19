(function() {
	angular.module('rateker.profile').
	service('Thoughts', [
		'Fetch',
		function(Fetch){

			this.next = null;

			var Thoughts = this;

			this.get = function() {
				return Fetch.get(Thoughts, 'thoughts');
			}


			this.next = function() {
				return Fetch.next(Thoughts, 'thoughts');
			}
		}]);
})();