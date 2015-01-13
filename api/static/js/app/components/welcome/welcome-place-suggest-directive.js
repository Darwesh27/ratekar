(function() {
	angular.module('rateker.welcome').
	directive('suggestPlace', [
		'http', 
		'welcomeConsts',
		'Welcome',
		'$timeout',
			function(http, welcomeConsts, Welcome, $timeout){
			// Runs during compile
			return {
				// name: '',
				// priority: 1,
				// terminal: true,
				scope: {
					place: "=",
				}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {},
				// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				templateUrl: welcomeConsts.baseTempUrl + "suggest-place.html",
				replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
				link: function($scope, iElm, iAttrs, controller) {

					$scope.tempName = "";

					var suggestions = iElm.find('.suggestions');

					var input = iElm.find('input');

					input.attr('tabIndex', iAttrs.tabIndex + 1);


					var isClicked = false;

					suggestions.hide();

					$scope.setPlace = function(suggestion) {
						console.log(suggestion);
						$scope.tempName = suggestion;
						$scope.place.name = suggestion;
					}


					$scope.$watch(
						function() {
							return $scope.tempName;
						},
						function(n, o) {

							if(n != null && n != undefined && n.length >= 3)
							{
								Welcome.suggestPlaces(n).then(
									function(data) {
										$scope.place.suggestions = angular.copy(data.places);
									},
									function(error) {
										$scope.place.suggestions = [];
									}
								);
							}
							else if(n.length < 3) {
								$scope.place.suggestions = [];
							}
						}
					);


					iElm.click(function(event) {

						if(input.val() != '' && input.val().length >= 3) {
							suggestions.show();
						}


					  	// if clicked on any of the suggestions then hide the dropdown..
					  	var suggs = iElm.find('.suggestion');

					  	angular.forEach(suggs, function(suggestion) {

					  		if(event.target == suggestion) {
					  			suggestions.hide();
					  		}
					  	})

					})

					input.blur(function(event) {

						$timeout(function() {
							if(!$scope.place.name.length > 0) {
								$scope.tempName = "";
							}
							else if($scope.place.name != $scope.tempName) {
								$scope.tempName = "";

								$scope.place.name = "";
							}
							suggestions.hide();
						}, 200);

					})

					input.focus(function() {
						$scope.tempName = $scope.place.name;
					})


					input.keyup(function(event) {

						if(input.val() == '' || input.val().length < 3) {
							suggestions.hide();
						}
						else {
							suggestions.show();
						}
					});



					$(document).on('click', function(event) {
					  if (!$(event.target).closest(iElm).length) {
					  	suggestions.hide();
					  }
					});			
				}
			};
	}]);
})();