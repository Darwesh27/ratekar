(function() {
	angular.module("rateker.profile").
	controller('nicksController', ['$scope', function($scope){
		$scope.nicks = [
			{
				name: "Sunny", 
				count: 20,
			},
			{
				name: "bunnY", 
				count: 1,
			},
			{
				name: "Jaidi", 
				count: 39,
			},
			{
				name: "Darwesh", 
				count: 10,
			},
			{
				name: "Sunto", 
				count: 7,
			},
		]
	}])
})();