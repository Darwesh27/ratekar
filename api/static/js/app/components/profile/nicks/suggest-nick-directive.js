(function() {
	angular.module('rateker.profile').
	directive('suggestNick', [
		'Profile',
	 	'Fetch', 
	 	'Nick',
	 	function(Profile, Fetch, Nick){
			// Runs during compile
			return {
				// name: '',
				// priority: 1,
				// terminal: true,
				// scope: {}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {},
				require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'A', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				// templateUrl: '',
				// replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {

					console.log(iElm.parent().children());

					$scope.$watch(
						function() {
							return $scope.newNick;
						}, 
						function(value) {
							if(value != '' && value != $scope.selectedNick) {
								Nick.suggest($scope.newNick).then(
									function(suggestions) {
										$scope.suggestions  = suggestions;
									}
								);

							}
						}
					);

				}
			};
		}]);
})();