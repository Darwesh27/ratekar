(function() {

	angular.module("rateker.profile").
	directive('review', ['profileConsts', function(profileConsts){
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			scope: {
				review: "=",

			}, // {} = isolate, true = child, false/undefined = no change
			controller: function($scope, $element, $attrs, $transclude) {
				$scope.toggleLike = function() {
					$scope.review.liked = !$scope.review.liked;
				};

				$scope.likeIcon = $scope.review.liked?"heart":"heart-outline";
			},
			// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
			restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
			// template: '',
			templateUrl: profileConsts.baseTempUrl + "reviews/review.html",
			replace: true,
			// transclude: true,
			// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
			link: function($scope, iElm, iAttrs, controller) {
				
			}
		};
	}]);
})();