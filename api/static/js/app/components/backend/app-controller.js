(function() {
	angular.module('rateker.backend').
	controller('appController', [
		'Me',
		'Auth', 
		'$scope', 
		'$interval',
		'$location', 
		'$rootScope',
		function(Me, Auth, $scope, $interval, $location, $rootScope){

			var urlBeforeLogin = null;
			$scope.isLoggedIn = Auth.isLoggedIn();
			$scope.isReady = Me.ready;

			$scope.$watch(function() {
				return Me.ready;
			},
			function(newVal, oldVal) {

				if(newVal == false) {
					$location.path('/welcome');
				}

				$scope.isReady = newVal;
			})


			// Me.checkReadiness().
			// then(function() {
			// 	$scope.$watch( function() {
			// 		return Auth.isLoggedIn();
			// 	}, function(value) {

			// 		$scope.isLoggedIn = value;
					
			// 		if(value == false) {
			// 			urlBeforeLogin = $location.path;
			// 			$location.path("/enter");
			// 		}
			// 	});

			// })

			$rootScope.$on('$stateChangeStart', function(event, toSt, toPr, frSt, frPr) {
				if(Auth.isLoggedIn() && toSt.url ==  "/enter"){
					event.preventDefault();
				}
				else if(!Auth.isLoggedIn() && toSt.url != "/enter") {
					event.preventDefault();
					$location.path("/enter");
				}

				if(!Me.ready && toSt.url != "/welcome") {
					event.preventDefault();
				}

			})


			$scope.$watch( function() {
				return Auth.isLoggedIn();
			}, function(value) {

				$scope.isLoggedIn = value;
				
				if(value == false) {
					console.log("Not logged in");
					Auth.beforeUrl = $location.path();
					$location.path("/enter");
				}
			});

	}]);
})();