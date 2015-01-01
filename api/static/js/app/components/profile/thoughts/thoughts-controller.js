(function() {
	angular.module('rateker.profile').
	controller('thoughtsController', [
		'$scope',
		'Thoughts', 
		'username',
		'$interval',
		 function($scope, Thoughts, username, $interval){


			Thoughts.init(username);

			$scope.thoughts = Thoughts.items;

			var fetchNextPosts = $interval(function() {
				Thoughts.fetchNext();
			}, 10000);


			$scope.$on('$destroy', function() {
				$interval.cancel(fetchNextPosts);
				Thoughts.destroy();
			});

			$scope.fetchPrevious = function() {
				$scope.end.hasNext = Thoughts.fetchPrevious();
			}

			$scope.end = {};
			$scope.end.message = "No more posts..";
			$scope.end.hasNext = true;

			$scope.$watch(function() {
				return Thoughts.previous;
			}, function(value) {
				if(value == null) {
					if(Thoughts.items.length > 0) {
						$scope.end.hasNext = false;
					}
				}
				else {
					$scope.end.hasNext = true;
				}
			});

		}]);
})();