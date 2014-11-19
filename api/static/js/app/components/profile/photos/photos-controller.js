(function() {
	angular.module('rateker.profile').
	controller('photosController', [
		'$scope',
		'Photos', 
		'Photo',
		'data',
		 function($scope, Thoughts, Thought, data){

		 	$scope.data = data;
		
		}]);
})();