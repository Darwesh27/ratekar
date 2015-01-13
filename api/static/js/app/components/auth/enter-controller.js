(function() {
	angular.module('rateker.auth').
	controller('EnterController', [
		'$scope', 
		'Dialog',
		function($scope, Dialog){

			$scope.showLoginPanel = function(ev) {
				Dialog.login(ev);
			};


			$scope.showSignUpPanel = function(ev) {
				Dialog.signUp(ev);
			};
	}])
})();