(function() {
	angular.module('rateker.stream.post').
	controller('NewPostController', [
		'$scope',
		'Fetch',
		'Urls',
		'Errors',
		'Stream',
		function($scope, Fetch, Urls, Errors, Stream){

			$scope.thought = "";
			$scope.touched = false 

			var goodToGo = function() {
				return !($scope.thought == null || $scope.thought == "")
			}

			$scope.share = function() {

				// If the post is valid
				if(goodToGo()) {

					var url = Urls.postStatus();
					var error = Errors.postStatus();
					var data = {
						thought: $scope.thought
					}


					var cb = function(data, q) {
						q.resolve(data);
					}

					var done = function(data) {
						// We have recieved the data 
						// Now add the new post to the beggining of the stream

						Stream.addNew(data.post);
						$scope.thought = "";
					}

					var notDone = function(error) {

					}

					Fetch.http('post', url, data, error, cb).then(done, notDone);
				}
			}


			$scope.cancel = function() {
				$scope.thought = "";
			}

		}]);
})();