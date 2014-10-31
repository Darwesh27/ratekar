(function() {
	angular.module("rateker.stream").
	controller('leftPaneController', ['$scope', function($scope){

		$scope.me = {
			name: "Malik Junaid",
			url: "/#/malik.junaid",
			imageUrl: "/static/img/mj2.jpg",
			reputation: 6.7,

		}
		
	}]);
})();