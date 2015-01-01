(function() {
	angular.module('rateker.stream').
	directive('detectEnd', [
		'$timeout', 
		'streamConsts', 
		'Stream',
		function($timeout, streamConsts, Stream) {
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			scope: {
				todo: "&",
				end: "="
			}, // {} = isolate, true = child, false/undefined = no change
			// controller: function($scope, $element, $attrs, $transclude) {},
			// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
			restrict: 'AE', // E = Element, A = Attribute, C = Class, M = Comment
			// template: '',
			templateUrl: streamConsts.baseTempUrl + "/stream-end.html",
			// replace: true,
			// transclude: true,
			// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
			link: function($scope, iElm, iAttrs, controller) {

				window.onscroll = function(ev) {
					angular.element('body').height(angular.element('.global-container').height() + 50);

				    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
				        // you're at the bottom of the page
				        
				        var fetching = $scope.todo();
				    }
				};
				
			}
		};
	}]);
})();