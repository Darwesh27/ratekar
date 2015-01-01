(function() {

	angular.module('rateker.backend').
	service('http', [
		'$http',
		'$q',
		function($http, $q){

			var http = this;


			this.get = function(url, error) {
				return general('get', url, null, error);
			}

			this.post = function(url, data, error) {
				return general('post', url, data, error);
			}

			var general = function(method, url, data, serverError) {

				var deffered = $q.defer();

				$http({method: method, url: url, data: data}).
				success(function(data) {
					if(!data.error) {
						deffered.resolve(data);
					}
					else {
						deffered.reject(data.error);
					}
				}).
				error(function(data) {
					deffered.reject(serverError);
				});

				return deffered.promise;
			}

		}]);
})();