(function() {
	angular.module('rateker.right-pane').
	directive('adjustRightPane',[
		'$timeout', 
		function($timeout){
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			// scope: {}, // {} = isolate, true = child, false/undefined = no change
			// controller: function($scope, $element, $attrs, $transclude) {},
			// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
			restrict: 'A', // E = Element, A = Attribute, C = Class, M = Comment
			// template: '',
			// templateUrl: '',
			// replace: true,
			// transclude: true,
			// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
			link: function($scope, iElm, iAttrs, controller) {

				var adjust = function() {
					var rightPaneBro = angular.element('.right-pane-bro');

					iElm.width(rightPaneBro.width());


					// Adjust toolbar's right side
					var toolbarRight = $('.toolbar-adjust-right');

					toolbarRight.width(rightPaneBro.width());
				}

				$scope.$on("$stateChangeSuccess" , function() {
					$timeout(function() {
						adjust();
					}, 1000);
				});

				$timeout(function() {
					adjust();
				}, 1000);

				angular.element(window).on('resize', function(e) {
					adjust();
				})
			}
		};
	}]);
})();