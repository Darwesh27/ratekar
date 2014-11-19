(function() {

	angular.module('rateker.backend').
	service('Fetch', [
		'$http',
		'Profile', 
		'$q', 
		'Urls',
		'Util',
		'Errors',
		function($http, Profile, $q, Urls, Util, Errors){

			var Fetch = this;


			this.http = function(method, url, data, serverError,cb) {
				var deffered = $q.defer();

				$http({method: method, url: url, data: data}).
				success(function(data) {
					if(!data.error) {
						cb(data, deffered);
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

			this.fetch = function(url, serverError, cb) {
				return Fetch.http('get', url , null, serverError, cb);
			}


			var getResource = function(caller, url, error) {

				var callback = function(data , q) {

					// Store the next url in serivce
					caller.next = data.next;


					// Tell the controller if it should ask for data or not..
					if(data.next != null) 
						data.next = true;
					else 
						data.next = false;

					q.resolve(data);
				}

				return Fetch.fetch(url, error, callback);

			}
			
			this.get = function(caller, resource) {

				return Urls.get(resource).then(
					function(url) {
						var error = Errors.profileError(resource, false);
						return getResource(caller, url, error);
					}
				);
			}


			this.next = function(caller, resource) {
				var url = caller.next;
				var error = Errors.profileError(resource, true);

				return getResource(caller, url, error);
			}


			this.getComments = function(postId) {

				url = Urls.comments(postId);
				error = Errors.profileError('comments', false);

				return Fetch.fetch(url, error, function(data, q) {
					q.resolve(data);
				});
			}

			this.nextComments = function(next) {
				error = Errors.profileError('comments', true);

				return Fetch.fetch(next, error, function(data, q) {
					q.resolve(data);
				})
			}





















		}]);
})();