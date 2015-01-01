(function() {
	angular.module('rateker.profile').
	directive('newFeedback', [
		'Feedback', 
		'profileConsts', 
		'$mdToast',
		function(Feedback, profileConsts, $mdToast){
			// Runs during compile
			return {
				// name: '',
				// priority: 1,
				// terminal: true,
				// scope: {}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {},
				// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				templateUrl: profileConsts.baseTempUrl + "feedbacks/new-feedback.html",
				// replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {

					$scope.error = null;

					$scope.toastPosition = {
						bottom: false,
						left: false,
						right: true,
						top: true,
					}


					 $scope.getToastPosition = function() {
					    var toret = Object.keys($scope.toastPosition)
					      .filter(function(pos) { return $scope.toastPosition[pos]; })
					      .join(' ');

					     return toret;
					  };

					var isOk = function() {
						return $scope.newFeedback && $scope.newFeedback.length > 3;
						// return false;
					}

					$scope.ask = function() {

						if(isOk()) {
							Feedback.create($scope.newFeedback).then(
								function(data) {

									$mdToast.show($mdToast.simple().content("New Feedback Added").hideDelay(500));

									$scope.newFeedback = null;
									$scope.error = null;

								}, 
								function(error) {
									$scope.error = error;
								}
							);
						}

					}
				}
		};
	}]);
})();