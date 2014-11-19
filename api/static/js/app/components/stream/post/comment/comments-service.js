(function() {
	
	angular.module('rateker.stream').
	service('Comments', [
		'Fetch',
		function(Fetch){

			this.next = null;

			var Comments = this;

			var Nicks = this;
		
			this.get = function(postId) {
				return Fetch.getComments(postId);
			}


			this.next = function(next) {
				return Fetch.nextComments(next);
			}
		}]);
})();