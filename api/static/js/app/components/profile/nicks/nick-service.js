(function() {
	angular.module('rateker.profile').
	service('Nick', [
		'$http',
		'Profile', 
		'Fetch',
		'Urls',
		'Errors',
		function($http, Profile, Fetch, Urls, Errors){

			this.suggest = function() {
				return Urls.get('suggestnicks').then(
					function(url) {
						var error = "Unable to fetch suggestions..";
						return Fetch.fetch(url, error, function(data, q) {
							q.resolve(data);
						});
					}
				);
			}

			this.get = function() {
				return Urls.nick().then(
					function(url){
						var error = "Unable to fetch the nick.. ";
						return Fetch.fetch(url, error, function(data, q) {
							q.resolve(data);
						});
					}
				);
			}

			this.give = function(nick) {

				return Urls.nick().then(
					function(url){
						data = {
							nick : nick,
						}
						var error = "Unable to update the nick.. ";
						return Fetch.http('post', url, data, error, function(data, q) {
							q.resolve(data);
						})
					}
				);


			}
		}]);
})();


