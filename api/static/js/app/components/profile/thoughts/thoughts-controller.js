(function() {
	angular.module('rateker.profile').
	controller('thoughtsController', [
		'$scope',
		'Thoughts', 
		'Thought',
		'data',
		 function($scope, Thoughts, Thought, data){

		 	$scope.data = data;
		
		}]);
})();