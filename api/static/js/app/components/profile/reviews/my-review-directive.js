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
				scope: {
					username: "@",
				}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {},
				// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				templateUrl: profileConsts.baseTempUrl + 'reviews/my-review.html',
				replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {


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


					var isOk = function() {
						return ($scope.newReview != null) && ($scope.newReview != '');
					}


					$scope.give = function() {
						if(isOk()) 
							Review.give($scope.newReview).then(yes, no);
					}


					$scope.canShow = function() {
						return $scope.available && !$scope.onEdit;
					}

					var yes = function(review) {

						if(review.text != "") {
							$scope.available = true;
							$scope.onEdit = false;
							$scope.myReview = review.text;
						}
						else {
							no();
						}

					}

					var no = function(data) {
						$scope.available = false;
						$scope.edit();
					}

					Review.get().then(yes, no);


				}
			};
		}]);
})();