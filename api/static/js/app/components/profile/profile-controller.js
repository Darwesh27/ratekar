(function() {

	angular.module("rateker.profile").
	controller('profileController', ['profileConsts','$scope', function(profileConsts, $scope){
		$scope.profile  = {
			name : "Malik Junaid",
			url: "/#/malik.junaid",
			imageUrl : "static/img/mj2.jpg",
			reputation: 6.7,
		}
	}])
})();