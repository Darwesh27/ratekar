(function() {
	angular.module('rateker.stream').
	service('Comment', [
		'Fetch',
		'Urls',
		'Errors', 
		function(Fetch, Urls, Errors){

			var cb = function(data, q) {
				q.resolve(data);
			}

			var gCondemn = function(commentId, condemn) {

				var url = Urls.condemnComment(commentId);
				var error = Errors.condemnComment();

				return Fetch.http('post', url,{condemn: condemn}, error, cb);
			}

			this.condemn = function(commentId) {
				return gCondemn(commentId, true);
			}

			this.unCondemn = function(commentId) {
				return gCondemn(commentId, false);
			}

			this.condemners = function(commentId) {

				url = Urls.commentCondemners(commentId);

				return Fetch.fetch(url, "", cb)
			}

			this.add = function(postId, comment) {

				url = Urls.newComment(postId);
				error = Errors.newComment();

				data = {
					text: comment
				}

				return Fetch.http("post", url, data, error, cb);

			}

		}]);
})();
