(function() {
	angular.module('rateker.backend').
	controller('appController', [
		'Me',
		'Auth', 
		'$scope', 
		'$interval',
		'$location', 
		function(Me, Auth, $scope, $interval, $location){
			$scope.isLoggedIn = Auth.isLoggedIn();

			$scope.$watch( function() {
				return Auth.isLoggedIn();
			}, function(value) {

				$scope.isLoggedIn = value;
				
				if(value == false) {
					$location.path("/enter");
				}
				else {
					$location.path("/");
				}
			});

	}]);
})();