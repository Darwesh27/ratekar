(function() {
	
	angular.module("rateker.rkToolbar").
	directive('toolbarSearch', [
		'toolbarConsts', 
		'searchService' ,
		'Me', 
		'$interval',
		function(toolbarConsts, searchService, Me, $interval){
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			scope: {},
			// {} = isolate, true = child, false/undefined = no change
			// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
			restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
			// template: '',
			templateUrl: toolbarConsts.baseTempUrl + "search/search.html",
			replace: true,
			// transclude: true,
			compile: function(tElement, tAttrs) {

				return {
					pre: function($scope, iElm, iAttrs, controller) {
						$scope.search  = "";
						$scope.message = "No results found..";
						$scope.showMessage = false;
					},

					post: function($scope, iElm, iAttrs, controller) {

						var dropdown = iElm.find('.search-results')

						dropdown.hide();


						$scope.$watch(function() {return $scope.search},
							function(value) {

								if(value != null && value != ""){

									iElm.find('.search-results').outerWidth(iElm.find('input').width());


									searchService.query(value).then(
										function(data) {
											dropdown.show();
											$scope.results = data.results;


											if(data.results.length <= 0) {
												$scope.showMessage = true;
											}
											else 
												$scope.showMessage = false;
										},
										function(error) {
											// Handle the error properly
										}
									);

								}
								else {
									$scope.results = [];
									dropdown.hide();
								}

							}
						);

						iElm.click(function() {
							if($scope.search != null && $scope.search != "")
								dropdown.show();
						})

						$(document).on('click', function(event) {
						  if (!$(event.target).closest(iElm).length) {
						  	dropdown.hide();
						  }
						});			
					}
				}
			},
		}
	}]);
})();