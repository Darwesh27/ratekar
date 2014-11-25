(function() {
	angular.module('rateker.rkToolbar.rkNotifications').
	directive('adjustCount', ['$timeout', function($timeout){
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

					var c = $(iElm);

					console.log(c);

					var count = iElm.children()[2];

					count = $(count);

					console.log(c.outerWidth());
					console.log(c.width());
					console.log(c.innerWidth());


					count.css({
						position: 'relative',
						top: '-2px',
						left: (c.outerWidth() - 10) + 'px'
					});

				}

				$timeout(function() {
					adjust();
				}, 2000);
			}
		};
	}]);
})();