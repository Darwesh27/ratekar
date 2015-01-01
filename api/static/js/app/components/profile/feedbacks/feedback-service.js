(function() {
	angular.module('rateker.profile').
	service('Feedback', [
		'http',
		'Profile', 
		'Fetch',
		'Urls',
		'Errors',
		function(http, Profile, Fetch, Urls, Errors){


			this.create = function(question) {
				var url = Urls.newFeedback();

				data = {
					text: question
				}

				return http.post(url,data, "Too short or already exists..");
			}

			this.get = function() {
				return Urls.get('feedback').then(
					function(url){
						var error = "Something went wrong in here.. ";
						return Fetch.fetch(url, error, function(data, q) {
							q.resolve(data);
						});
					}
				);
			}

			this.give = function(feedback) {

				return Urls.get('feedback').then(
					function(url){
						var data = {
							id: feedback.id,
							rating: feedback.rating
						}
						var error = "Something went wrong here ";
						return Fetch.http('post', url, data, error, function(data, q) {
							q.resolve(data);
						})
					}
				);
			}

			this.skip = function(exclude) {
				return Urls.get('feedback').then(
					function(url){
						var data = {
							exclude: exclude,
						}
						var error = "Something went wrong here ";
						return Fetch.http('post', url, data, error, function(data, q) {
							q.resolve(data);
						})
					}
				);

			}
		}]);
})();