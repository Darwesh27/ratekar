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

					var exclude = [];

					prevIds = [];


					// Indicates that the new feedback's rating is same as the old one..
					// due to which the $watch didn't catch it..
					var masla = false;


					// Indicates that recent change in rating is due to arrival of new question 
					var update = true;

					// This is the flag to prevent calling $watch for rating before the first get call
					var recieving = true;

					var showFeedback = function(data) {

						update = true;

						if(!recieving) {
							masla = data.feedback.rating == $scope.feedback.rating;
						}
						else {
							update = false;
						}

						$scope.feedback = data.feedback;
						recieving = false;
					}

					var showError = function(error) {
						$scope.error = error;
					}

					$scope.skip = function() {

						console.log(exclude);
						if(!($scope.feedback.id in exclude))
							exclude.push($scope.feedback.id);

						Feedback.skip(exclude).then(showFeedback, showError);


					}

					$scope.$watch(
						function() {
							if(!recieving)
								return $scope.feedback.rating;
						}, 
						function(n, o) {

							// console.log("From ");
							// console.log(o);
							// console.log(" to ");
							// console.log(n);

							if (o != undefined) {

								if(!update) {
									if($scope.feedback.id in exclude) {
										exclude.splice(exclude.indexOf($scope.feedback.id, 1));
									}

									Feedback.give($scope.feedback).then(showFeedback, showError);

									console.log("rating is changed");
								}
								else if (update) {
									if(masla) {
										if($scope.feedback.id in exclude) {
											exclude.splice(exclude.indexOf($scope.feedback.id, 1));
										}

										Feedback.give($scope.feedback).then(showFeedback, showError);

										console.log("New rating was same.. Now changed..");
									}

									else {
										console.log("this is due to new arrival");
										update = false;
									}
								}
							}
							else {
								console.log("Old was undefined");
							}


						}
					);

					Feedback.get().then(showFeedback, showError);
				}
			};
		}]);
})();