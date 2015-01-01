(function () {
		
	angular.module("rateker.rkToolbar.rkNotifications").
	directive('friendRequests', [
		'notiConsts', 
		'notificationsService', 
		function(notiConsts, notificationsService){
		// Runs during compile
			return {
				// name: '',
				// priority: 1,
				// terminal: true,
				scope: {
					friendRequests: "="
				}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {
				// },
				// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				templateUrl: notiConsts.baseTempUrl + "friend-requests.html",
				replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {

					$scope.done = function(index) {

						var username = $scope.friendRequests.items[index].username;

						$scope.friendRequests.count -= 1;
						$scope.friendRequests.items.splice(index, 1);


						$scope.friendRequests.old.splice($scope.friendRequests.old.indexOf(username), 1)

					}
					
				}
			};
		}]);
})();