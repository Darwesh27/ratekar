(function() {
	angular.module('rateker.auth').
	directive('checkEmail', [
		'Fetch', 
		'Urls',
		'Errors',
		 function(Fetch, Urls, Errors){
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
				// templateUrl: '',
				// replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {


					var check = function(value) {
						url = Urls.checkEmail();
						error = "Unable to check email..";
						data = {
							email: value 
						}

						Fetch.http('post', url, data, error, function(data, q) {
							q.resolve(data);
						}).then(
							function(availibility) {
							if(availibility.exists) {
									$scope.emailBad = true;
									$scope.emailGood = false;
								}
								else {
									$scope.emailGood = true;
									$scope.emailBad = false;
								}
							},
							function(error) {
								// Handle the error
							},
							function() {
								// Handle when fetching is being done..
							}
						);
					}
					
					$scope.$watch(
						function() {
							return $scope.signup.email;
						}, 
						function(value) {

							if((value != null) && (value != '')) {
								check(value);
							}
							else {
								$scope.emailGood = false;
								$scope.emailBad = false;
							}
						}
					);
				}
			};
		}]);
})();