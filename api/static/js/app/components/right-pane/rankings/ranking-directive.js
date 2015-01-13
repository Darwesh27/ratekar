(function() {
	angular.module('rateker.right-pane').
	directive('ranking', [
		'rightPaneConsts', 
		function(rightPaneConsts){
			// Runs during compile
			return {
				// name: '',
				// priority: 1,
				// terminal: true,
				scope: {
					ranking: "="
				}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {},
				// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				templateUrl: rightPaneConsts.baseTempUrl + 'rankings/ranking.html',
				replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {
					
				}
			};
	}]);
})();