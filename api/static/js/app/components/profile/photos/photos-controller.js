(function() {
	angular.module('rateker.profile').
	controller('photosController', [
		'$scope',
		'Photos', 
		'Photo',
		'username',
		 function($scope, Thoughts, Thought, username){

		 	$scope.data = username;
		
		}]);
})();