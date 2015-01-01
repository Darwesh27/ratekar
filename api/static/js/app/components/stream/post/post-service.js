(function  () {

	angular.module("rateker.stream.post").
	service('Post', [
		'Fetch',
		'Urls',
		'Errors',
		function(Fetch, Urls, Errors){

			this.rate = function(postId, rating) {

				url = Urls.ratePost(postId);
				error = Errors.ratePost(postId);
				data = {
					rating: rating
				}

				return Fetch.http('post', url, data, error, function(data, q) {
					q.resolve(data);
				})
			}
		}]);
})();