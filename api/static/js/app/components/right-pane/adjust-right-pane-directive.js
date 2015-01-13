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


					var globalContainer = angular.element('.global-container');
					var rightPaneBro = angular.element('.right-pane-bro');

					var adjusts = angular.element('.adjust-width');

					var width = globalContainer.width()

					// console.log(width);

					if( width >= 1210) {
						var space = width - 960;
						var offset = (space - 190) / 2;
						var rightPaneWidth = 200 + offset;


						angular.forEach(adjusts, function(adjust) {
							angular.element(adjust).width(offset);
						});
						rightPaneBro.width(rightPaneWidth);
						iElm.width(rightPaneWidth);
						
						// Adjust toolbar's right side
						var toolbarRight = $('.toolbar-adjust-right');

						toolbarRight.width(rightPaneWidth);

						var rankings = angular.element('.rankings');
						rankings.show();

					}
					else {

						var offset = width - 960;

						// Set the width of right pane bro.. right pane and adjusts
						angular.forEach(adjusts, function(adjust) {
							console.log(adjust);
							angular.element(adjust).width(offset / 2);
						});

						iElm.width(offset / 2);
						rightPaneBro.width(offset / 2);

						// Adjust toolbar's right side
						var toolbarRight = $('.toolbar-adjust-right');

						toolbarRight.width(offset / 2);

						var rankings = angular.element('.rankings');
						rankings.hide();

					}



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