(function() {
	angular.module('rateker.profile').
	controller('thoughtsController', [
		'$scope',
		'Thoughts', 
		'Thought',
		'data',
		 function($scope, Thoughts, Thought, data){

		 	console.log("Chaliyae");

		 	$scope.data = data;
		
		}]);
})();