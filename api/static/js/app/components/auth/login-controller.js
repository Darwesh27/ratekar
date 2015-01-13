(function() {
	angular.module("rateker.auth").
	controller('LoginController', [
		'$scope', 
		'Auth', 
		'$mdDialog',
		'Dialog',
		function($scope, Auth, $mdDialog, Dialog){

			$scope.error  = "";
			$scope.cred = null;
			$scope.pass = null;

			var formValid = function  () {
				return !(($scope.cred == null || $scope.cred == "") && ($scope.pass == null || $scope.pass == ""))
			}
			
			$scope.logIn = function() {


				if(formValid()) {
					// $mdDialog.hide();
					Auth.logIn($scope.cred, $scope.pass, function(err) {

						if(err) {
							$scope.error = err;
						}
					});

				}

			}

			$scope.signUpInstead = function() {

				$mdDialog.hide();

				Dialog.signUp();
			}
	}]);
})();