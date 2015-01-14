(function() {
	angular.module('rateker.welcome').
	directive('welcomeSuggestions', [
		'http', 
		'welcomeConsts', 
		'Urls',
		'Errors',
		function(http, welcomeConsts, Urls, Errors){
			// Runs during compile
			return {
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				controller: function($scope, $element, $attrs, $transclude) {

					this.add = function(index) {
						$scope.suggestions.splice(index, 1);
					}
				},
				templateUrl: welcomeConsts.baseTempUrl + "welcome-suggestions.html",
				replace: true,
				link: function($scope, iElm, iAttrs, controller) {

					$scope.suggestions = []

					// These shouldn't be fetched anymore
					var exclude = [];

					// Do we have more suggestions
					var next = false;

					var addTosuggestions = function(data) {
						if(data.next) 
							next = data.next

						angular.forEach(data.suggestions, function(s) {
							$scope.suggestions.push(s);

							exclude.push(s.username);
						})
					}

					var get = function() {
						var url = Urls.friendSuggestions();
						var error = Errors.friendSuggestions();

						http.get(url, error).then(addTosuggestions);
					}

					var getNext = function() {
						if(next) {
							var url = Urls.friendSuggestions();
							var error = Errors.friendSuggestions();
							var data = {
								exclude: exclude,
							}

							http.post(url, data, error).then(addTosuggestions);
						}
					}

					var getSuggestions = function() {
						get();
					}


					// Fetch suggestions 
					getSuggestions();

					// Fetch more suggestions when the end has reaaced
					iElm.bind('scroll', function() {
						if($(this).scrollTop() + $(this).innerHeight() >= this.scrollHeight) {
							getNext();
				        }
					});
				}
			};
	}]);
})();