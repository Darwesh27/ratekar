(function() {
	angular.module('rateker.stream').
	directive('friendSuggestion', [
		'streamConsts', 
		function(streamConsts){
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			scope: {
				suggestion: "=",
				index: "&",
			}, // {} = isolate, true = child, false/undefined = no change
			// controller: function($scope, $element, $attrs, $transclude) {},
			require: '^friendSuggestions', // Array = multiple requires, ? = optional, ^ = check parent elements
			// restrict: 'A', // E = Element, A = Attribute, C = Class, M = Comment
			// template: '',
			templateUrl: streamConsts.baseTempUrl + 'suggestions/friend-suggestion.html',
			replace: true,
			// transclude: true,
			// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
			link: function($scope, iElm, iAttrs, controller) {
				
				$scope.check = "Hello123lsdfkjslfweeofljxlk";
				$scope.add = function() {
					controller.add($scope.index());
				}

				$scope.skip = function() {
					controller.skip($scope.index());
				}

				
			}
		};
	}]);
})();