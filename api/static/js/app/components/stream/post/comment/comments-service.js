(function() {
	
	angular.module('rateker.stream').
	service('Comments', [
		'Fetch',
		'Urls',
		'Errors',
		function(Fetch, Urls, Errors){

			this.next = null;

			var Comments = this;

			this.get = function(postId) {
				url = Urls.comments(postId);
				error = Errors.profileError('comments', false);

				return Fetch.fetch(url, error, function(data, q) {
					q.resolve(data);
				});
			}


			this.next = function(postId, next, befNext) {
				url = Urls.nextComments(postId, next, befNext);
				error = Errors.profileError('comments', true);

				return Fetch.fetch(url, error, function(data, q) {
					q.resolve(data);
				})
			}

			this.previous = function(postId, previous, befPrev) {
				url = Urls.previousComments(postId, previous, befPrev);
				error = Errors.profileError('comments', true);

				return Fetch.fetch(url, error, function(data, q) {
					q.resolve(data);
				})

			}
		}]);
})();