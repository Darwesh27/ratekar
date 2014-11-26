(function() {
	angular.module('rateker.dropdown').
	directive('rkDropdown', [
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
				// restrict: 'A', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				// templateUrl: '',
				// replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				compile: function(tElement, tAttrs) {

					var caret = "";
					caret += "<div class='dropdown-caret'>";
					caret += "<span class='caret-outer'></span>";
					caret += "<span class='caret-inner'></span>";
					caret += "</div>";

					var temp = "";
					temp += "<div class='rk-dropdown rk-dropdown-toolbar'>";
					temp += caret;
					temp += "<div class='rk-dropdown-menu'>";
					temp += "</div>";
					temp += "</div>";

					tElement.append(angular.element(temp));

					return {
						pre: function($scope, iElm, iAttrs, controller) {

						},
						post: function($scope, iElm, iAttrs, controller) {

							iElm.click(function() {
								var last = iElm.children().length - 1;
								angular.element(iElm.children()[last]).toggleClass('show-menu');
							});
						}
					}
				},
				link: function($scope, iElm, iAttrs, controller) {

				}
			};
		}]);
})();