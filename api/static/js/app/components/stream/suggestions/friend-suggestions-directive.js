(function() {
	angular.module('rateker.stream').
	directive('friendSuggestions', [
		'FriendSuggestions', 
		'streamConsts',
		'$timeout',
		function(FriendSuggestions, streamConsts, $timeout){
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			scope: {}, // {} = isolate, true = child, false/undefined = no change
			controller: ['$scope', '$element', '$attrs', '$transclude', function($scope, $element, $attrs, $transclude) {

				this.add = function(index) {


					// var sugg = $scope.suggestions[index];

					// remove the element
					$scope.suggestions.splice(index, 1);


					FriendSuggestions.next($scope.exclude).then(
						function(data) {
							angular.forEach(data, function(suggestion){
								$scope.suggestions.push(suggestion);
								$scope.exclude.push(data.username);
							});


						},
						function(error) {
							$scope.error = error;
						}
					);
				}

				this.skip = function(index) {

				}

			}],
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