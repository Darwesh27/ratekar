(function() {
	angular.module('rateker.stream.post').
	directive('newPost', [
		'Profile', 
		'postConsts',
		function(Profile, postConsts){
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
				templateUrl: postConsts.baseTempUrl + "new/new-post.html",
				replace: true,
				// transclude: true,
				compile: function(tElement, tAttrs) {

					return {
						pre: function($scope, iElm, iAttrs, controller) {

						},
						post: function($scope, iElm, iAttrs, controller) {

							iElm.click(function() {
								$scope.touched = true;
							})

							$(document).on('click', function(event) {
								if (!$(event.target).closest(iElm).length) {
									$scope.touched = false;
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