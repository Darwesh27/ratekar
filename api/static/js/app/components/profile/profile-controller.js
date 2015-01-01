(function() {

	angular.module("rateker.profile").
	controller('profileController', [
		'profileConsts',
		'$scope', 
		'Me',
		'Profile',
		'$stateParams',
		'$route',
		'$interval',
		'$timeout',
		'profile',
		function(profileConsts, $scope, Me, Profile, $stateParams, $route, $interval, $timeout, profile){

			// profile.then(
			// 	function(profile) {
			// 		$scope.profile = profile;
			// 	},
			// 	function(error) {
			// 		$scope.error = error;
			// 	}
			// );


			$scope.available = true;

			if(profile.error) {
				$scope.available = false;
			}
			else {
				$scope.available = true;
				$scope.profile = profile;
			}

			$scope.$watch(function() {
				return $scope.profile.reputation.my;
			}, function(n, o) {
				if(n!=o) {
					Profile.rate($scope.profile, n);
				}
			});

			$scope.errorPageUrl = "/static/js/app/components/profile/error.html";

		}]);
})();