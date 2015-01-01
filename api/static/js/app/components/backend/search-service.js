(function() {
	angular.module("rateker.backend").
	service('searchService', [
		'$http', 
		'Urls',
		'Fetch', 
		function($http, Urls, Fetch){

		this.query = function(input) {
			url = Urls.search(input);
			error = "Can't search";

			return Fetch.fetch(url, error, function(data,q){q.resolve(data)});
		}
	}]);
})();