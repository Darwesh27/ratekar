(function() {
	angular.module("rateker.auth").
	controller('loginController', ['$scope', 'Auth', function($scope, Auth){

		$scope.error  = "";
		$scope.cred = null;
		$scope.pass = null;

		var formValid = function  () {
			return !(($scope.cred == null || $scope.cred == "") && ($scope.pass == null || $scope.pass == ""))
		}
		
		$scope.logIn = function() {

			if(formValid()) {
				Auth.logIn($scope.cred, $scope.pass, function(err) {

					if(err) {
						$scope.error = err;
					}
				});

			}

		}
	}]);
})();