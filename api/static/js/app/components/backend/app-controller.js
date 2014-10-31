(function() {
	angular.module('rateker.backend').
	controller('appController', ['Auth', '$scope' , function(Auth, $scope){
		$scope.isLoggedIn = Auth.isLoggedIn();
	}]);
})();