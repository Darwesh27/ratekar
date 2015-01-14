(function() {
	angular.module('rateker.welcome').
	directive('welcomeSuggestion', [
		'welcomeConsts', 
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
			require: '^welcomeSuggestions', // Array = multiple requires, ? = optional, ^ = check parent elements
			// restrict: 'A', // E = Element, A = Attribute, C = Class, M = Comment
			// template: '',
			templateUrl: streamConsts.baseTempUrl + 'welcome-suggestion.html',
			replace: true,
			// transclude: true,
			// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
			link: function($scope, iElm, iAttrs, controller) {

				iElm.hover(function() {
					iElm.find('.friend-suggestion-skip').show();
				},
				function() {
					iElm.find('.friend-suggestion-skip').hide();
				});

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