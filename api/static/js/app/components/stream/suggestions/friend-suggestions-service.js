(function() {
	angular.module('rateker.stream').
	service('FriendSuggestions', [
		'Urls', 
		'Errors', 
		'Fetch', 
		function(Urls, Errors, Fetch){

			this.get = function() {

				var url = Urls.friendSuggestions();
				var error = Errors.friendSuggestions();

				return Fetch.fetch(url, error, function(data, q) {
					q.resolve(data);
				});
			}


			this.next = function(exclude) {
				var url = Urls.friendSuggestions();
				var error = Errors.friendSuggestions();

				var data = {
					exclude: exclude,
				}

				return Fetch.http('post', url, data, error, function(data, q) {
					q.resolve(data);
				});
			}
		
		}]);
})();