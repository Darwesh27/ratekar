(function () {
		
	angular.module("rateker.rkToolbar.rkNotifications").
	directive('notifications', [
		'notiConsts', 
		'notificationsService', 
		function(notiConsts, notificationsService){
		// Runs during compile
			return {
				// name: '',
				// priority: 1,
				// terminal: true,
				scope: {
					notifications: "="
				}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {
				// },
				// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				templateUrl: notiConsts.baseTempUrl + "notifications.html",
				replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {

					$scope.readAll = function() {
						notificationsService.readAll();
					}
				}
			};
		}]);
})();