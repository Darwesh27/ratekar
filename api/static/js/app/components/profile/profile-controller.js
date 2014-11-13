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

			$scope.profile = profile;

		}]);
})();