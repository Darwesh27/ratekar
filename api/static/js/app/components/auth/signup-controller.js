(function() {
	angular.module("rateker.auth").
	controller('SignUpController', [
		'$http', 
		'$scope', 
		'Auth', 
		'$mdDialog',
		'Dialog',
		function($http, $scope, Auth, $mdDialog, Dialog){
		$scope.signup = {};
		$scope.signup.firstname = null;
		$scope.signup.lastname = null;
		$scope.signup.username = null;
		$scope.signup.email = null;
		$scope.signup.password = null;

		$scope.uNameGood = false;
		$scope.uNameBad = false;

		$scope.emailGood = false;
		$scope.emailBad = false;

		$scope.requested = false;


		var formValid = function() {
			angular.forEach($scope.signup, function(value, key) {
				if(value == null || value == "")
					return false;
			});
			
			return true;
		}


		$scope.signUp = function() {


			if(!$scope.requested) {
				if(formValid()) {

					$scope.requested = true;

					Auth.signUp($scope.signup).then(
						function(data){
							$scope.requested = false;
						},
						function(err) {
							$scope.error = err;
							$scope.requested = false;
						}
					);
				}
				else {
					$scope.error = "Fill all the info please";
				}

			}

		}

		$scope.loginInstead = function() {

			$mdDialog.hide();

			Dialog.login();
		}
	}]);
})();