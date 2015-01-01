(function () {
		
	angular.module("rateker.rkToolbar.rkNotifications").
	directive('toolbarMessages', [
		'notiConsts', 
		'notificationsService', 
		function(notiConsts, notificationsService){
		// Runs during compile
			return {
				// name: '',
				// priority: 1,
				// terminal: true,
				scope: {
					messages: "="
				}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {
				// },
				// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				templateUrl: notiConsts.baseTempUrl + "toolbar-messages.html",
				replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				// link: function($scope, iElm, iAttrs, controller) {
					
				// }
			};
		}]);
})();