(function() {
	angular.module('rateker.profile').
	directive('myReview', [

		'profileConsts',
		'Profile', 
		'Review', 
		function(profileConsts, Profile, Review){
			// Runs during compile
			return {
				// name: '',
				// priority: 1,
				// terminal: true,
				scope: {}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {},
				// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				templateUrl: profileConsts.baseTempUrl + 'reviews/my-review.html',
				replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {

					var textarea = angular.element(iElm.children[2]);

					console.log(textarea);
					console.log(textarea.offset());

					$scope.keyUp = function(e) {
						console.log("Hello");

						console.log(textarea.innerHeight());
					}


					console.log(iElm.children()[2]);


					$scope.profile = Profile.profile;

					$scope.onEdit = false;

					$scope.available = false;


					$scope.edit = function() {

						$scope.onEdit = true;
						$scope.newReview = '';

					}

					$scope.cancel = function(){

						$scope.newReview = '';

						if($scope.available) {
							$scope.onEdit = false;
						}
					}


					$scope.give = function() {
						Review.give($scope.newReview).then(yes, no);
					}


					$scope.canShow = function() {
						return $scope.available && !$scope.onEdit;
					}

					var yes = function(data) {

						$scope.available = true;
						$scope.onEdit = false;
						$scope.myReview = data.review;
					}

					var no = function(data) {
						$scope.available = false;
					}

					Review.get().then(yes, no);


				}
			};
		}]);
})();