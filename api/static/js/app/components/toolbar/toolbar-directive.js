(function  () {
	angular.module("rateker.rkToolbar").
	directive('rkToolbar', [
		'toolbarConsts', 
		'Me',
		function(toolbarConsts, Me){
		return {
			// scope: {}, // {} = isolate, true = child, false/undefined = no change
			// controller: function($scope, $element, $attrs, $transclude) {},
			// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
			restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
			// template: '',
			templateUrl: toolbarConsts.baseTempUrl + "toolbar.html",
			replace: true,
			// transclude: true,
			// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
			link: function($scope, iElm, iAttrs, controller) {

				$scope.user = Me.user;

				Me.getUser().then(function(user) {
					$scope.user = user;
				})
			}
		};
	}]);
})();