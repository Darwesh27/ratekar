(function() {
	angular.module("rateker.profile").
	controller('nicksController', [
		'$scope', 
		'Nicks',
		'Nick',
		'username',
		function($scope, Nicks, Nick, username){

			Nicks.init(username);
			Nick.init(username);

			$scope.nicks = Nicks.items;

			$scope.dicks = [
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