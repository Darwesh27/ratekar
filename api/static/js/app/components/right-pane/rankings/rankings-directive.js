(function() {
	angular.module('rateker.right-pane').
	directive('rankings', [
		'rightPaneConsts', 
		"Urls",
		'http',
		'$interval',
		function(rightPaneConsts, Urls, http, $interval){
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
				templateUrl: rightPaneConsts.baseTempUrl + 'rankings/rankings.html',
				replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {

					var url = Urls.rankings();

					var updateRankings = function() {

						http.get(url, '').then(
							function(data) {
								$scope.rankings = data.rankings;
							},
							function(error) {
								// Handle the fucking error..
							}
						)

					}

					updateRankings();

					var update = $interval(function() {
						updateRankings();
					}, 60000)

					$scope.$on("$destroy" , function() {
						$interval.cancel(update);
					});

				}
			};
	}]);
})();