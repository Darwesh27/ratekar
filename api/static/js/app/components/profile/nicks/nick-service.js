(function() {
	angular.module('rateker.profile').
	service('Nick', [
		'$http',
		'Profile', 
		'Fetch',
		'Urls',
		'Errors',
		'http',
		function($http, Profile, Fetch, Urls, Errors, http){

			var Nick = this;

			this.init = function(username) {
				this.username = username;
			}

			this.suggest = function(text) {
				url = Urls.suggestNicks(Nick.username);
				var error = "Unable to fetch suggestions..";

				data = {
					text: text,
				}

				return http.post(url, data, error);
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


