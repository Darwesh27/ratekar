(function() {
	angular.module("rateker.stream").
	controller('leftPaneController', [
		'$scope', 
		'Me',
		function($scope, Me){

			$scope.me = Me.user;
		
	}]);
})();