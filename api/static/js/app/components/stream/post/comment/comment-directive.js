(function() {

	angular.module("rateker.stream.post").
	directive('rkComment', [
		'postConsts', 
		'Comment',
		function(postConsts, Comment){
			// Runs during compile
			return {
				// name: '',
				// priority: 1,
				// terminal: true,
				scope: {
					comment: "="
				}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {},
				// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				templateUrl: postConsts.baseTempUrl + "/comment/comment.html",
				replace: true,
				// transclude: true,
				// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),


				compile: function(tElem, tAttrs) {

					return {
						pre: function($scope, iElm, iAttrs) { 
							$scope.condemn = {};


							$scope.condemn.text = ($scope.comment.condemned)?"unBad":"Bad";
							$scope.condemn.procedure = ($scope.comment.condemned)?unCondemnComment:condemnComment;
							$scope.condemn.tooltip = ($scope.comment.condemned)?"unCondemn":"Condemn";

							var unCondemnComment = function() {
								Comment.unCondemn($scope.comment.id).then(
									function(data) {
										$scope.comment = data.comment;
										$scope.condemn.text = "Bad";
									},
									function(error) {

									}
								);
							}

							var condemnComment = function() {
								Comment.condemn($scope.comment.id).then(
									function(data) {
										$scope.comment = data.comment;
										$scope.condemn.text = "unBad";
									},
									function(error) {

									}
								);
							}

							$scope.$watch(
								function() {
									return $scope.condemn.text;
								},
								function(value) {
									$scope.condemn.procedure = (value == "unBad")?unCondemnComment:condemnComment;
									$scope.condemn.tooltip = (value == "unBad")?"unCondemn":"Condemn";
								}
							);







						},
						post: function(scope, iElm, iattrs) { 

							Comment.condemners(scope.comment.id).then(
								function(data) {
									scope.comment.condemners = data.condemners;
								}
							);

						}
					}
				},
				link: function($scope, iElm, iAttrs, controller) {

					
				}
			};
		}]);
})();