(function() {
	angular.module('rateker.stream').
	directive('friendSuggestions', [
		'FriendSuggestions', 
		'streamConsts',
		function(FriendSuggestions, streamConsts){
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			scope: {}, // {} = isolate, true = child, false/undefined = no change
			controller: function($scope, $element, $attrs, $transclude) {

				this.add = function(index) {

					var sugg = $scope.suggestions[index];

					// remove the element
					$scope.suggestions.splice(index, 1);

					FriendSuggestions.next("Hello").then(
						function(data) {
							$scope.suggestions.push(data);
							$scope.exclude.push(data.username);

						},
						function(error) {
							$scope.error = error;
						}
					);
				}

				this.skip = function(index) {

				}

			},
			// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
			// restrict: 'A', // E = Element, A = Attribute, C = Class, M = Comment
			// template: '',
			templateUrl: streamConsts.baseTempUrl + 'suggestions/friend-suggestions.html',
			replace: true,
			// transclude: true,
			compile: function(tElement, tAttrs) {
				return {
					pre: function(scope, iElm, iAttrs) {

						var addToExclude = function(suggestions) {
							scope.exclude = [];

							angular.forEach(suggestions, function(suggestion) {
								scope.exclude.push(suggestion.username);
							});
						}

						var showSuggestions = function(suggestions) {
							scope.suggestions = suggestions;
							addToExclude(suggestions);
						}

						var showErrors = function(error) {
							scope.error = error;
						}

						FriendSuggestions.get().then(showSuggestions, showErrors);
					},

					post: function(scope, iElm, iAttrs) {

					}
				}
			},
			link: function($scope, iElm, iAttrs, controller) {
				
			}
		};
	}]);
})();