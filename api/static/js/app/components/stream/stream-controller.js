(function  () {

	angular.module("rateker.stream").
	controller('StreamCtrl', [
		'$scope', 
		'$routeParams', 
		'Stream',
		'$interval',
		'Dialog',
		function($scope, $routeParams, Stream, $interval, Dialog) {



			$scope.posts = Stream.posts;

			Stream.init();

			var fetchNextPosts = $interval(function() {
				Stream.fetchNext();
			}, 10000);


			$scope.$on('$destroy', function() {
				$interval.cancel(fetchNextPosts);

				Stream.destroy();
			});

			$scope.fetchPrevious = function() {
				Stream.fetchPrevious();
			}

			$scope.showDialog = function(ev, postId) { 
				Dialog.post(ev, postId);
			}


		}]);
})();