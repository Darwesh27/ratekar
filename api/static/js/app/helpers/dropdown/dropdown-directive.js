(function() {
	angular.module('rateker.dropdown').
	directive('dropdown', [
		'$timeout', 
		'dropdownConsts',
		function($timeout, dropdownConsts){
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
				templateUrl: dropdownConsts.baseTempUrl + "dropdown.html",
				replace: true,
				transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				compile: function(tElement, tAttrs) {

					return {
						pre: function($scope, iElm, iAttrs, controller) {

						},
						post: function($scope, iElm, iAttrs, controller) {

							var parent = angular.element(iElm.parent());

							var elem = angular.element(parent.children()[0]);

							elem.click(function(){
								iElm.toggleClass('show-menu');
							})

							$(document).on('click', function(event) {
							  if (!$(event.target).closest(parent).length) {
							  	iElm.removeClass('show-menu');
							  }
							});

						}
					}
				},
				link: function($scope, iElm, iAttrs, controller) {

				}
			};
		}]);
})();