(function() {
	angular.module("rateker.backend").
	controller('signupController', [
		'$http', 
		'$scope', 
		'Auth', 
		function($http, $scope, Auth){
		$scope.signup = {};
		$scope.signup.firstname = null;
		$scope.signup.lastname = null;
		$scope.signup.username = null;
		$scope.signup.email = null;
		$scope.signup.password = null;

		var formValid = function() {
			angular.forEach($scope.signup, function(value, key) {
				if(value == null || value == "")
					return false;
			});
			
			return true;
		}


		$scope.signUp = function() {
			if(formValid()) {
				console.log("Form valid");
				Auth.signUp($scope.signup, function(err){
					$scope.error = err;
				});
			}
			else {
				$scope.error = "Fill all the info please";
			}
		}
	}]);
})();