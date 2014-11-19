(function() {
	angular.module('rateker.profile').
	directive('myNick', [
		'profileConsts',
		 'Profile', 
		 'Nick', 
		 function(profileConsts, Profile, Nick){
			// Runs during compile
			return {
				// name: '',
				// priority: 1,
				// terminal: true,
				scope: {}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {},
				// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				templateUrl: profileConsts.baseTempUrl + 'nicks/my-nick.html',
				replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {


					$scope.profile = Profile.profile;

					$scope.available = false;

					$scope.noNick = false;


					$scope.edit = function() {

						$scope.onEdit = true;
						$scope.newNick = '';

					}


					$scope.select = function(suggestion) {
						$scope.newNick = suggestion;
						$scope.selectedNick = suggestion;
						$scope.suggestions = null;
					}

					$scope.cancel = function(){

						$scope.newNick = '';

						if($scope.available) {
							$scope.onEdit = false;
						}
					}


					$scope.give = function() {
						Nick.give($scope.newNick).then(yes, no);
					}


					$scope.noNick = function() {
						return $scope.onEdit;
					}


					$scope.canShow = function() {
						return $scope.available && !$scope.onEdit;
					}

					var yes = function(data) {

						$scope.available = true;
						$scope.onEdit = false;
						$scope.myNick = data.nick;

					}

					var no = function(data) {
						$scope.available = false;
					}

					Nick.get().then(yes, no);
				}
			};
		}]);
})();