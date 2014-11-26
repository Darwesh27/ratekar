(function() {
	angular.module('rateker.profile').
	directive('myFeedback', [
		'profileConsts', 
		'Profile', 
		'Feedback', 
		function(profileConsts, Profile, Feedback){
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
				templateUrl: profileConsts.baseTempUrl + 'feedbacks/my-feedback.html',
				// replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {

					$scope.profile = Profile.profile;

					$scope.feedback = null;


					$scope.myRating = null;

					var update = true;
					var recieving = true;

					var showFeedback = function(data) {

						update = true;
						recieving = false;
						$scope.feedback = data;
					}


					var showError = function(error) {
						$scope.error = error;
					}

					$scope.skip = function() {
						Feedback.skip($scope.feedback).then(showFeedback, showError);
					}


					$scope.$watch(
						function() {
							if(recieving) {

								// return zero beacuse feedback is 1-5 so it will change and event 
								// will be fired..
								return 0;
							}
							else {
								return $scope.feedback.rating;
							}
						}, 
						function(value) {
							if(!update) {
								Feedback.give($scope.feedback).then(showFeedback, showError);
							}
							else {
								update = false;
							}
						}
					);

					Feedback.get().then(showFeedback, showError);
				}
			};
		}]);
})();