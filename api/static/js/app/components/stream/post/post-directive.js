(function  () {
	
	angular.module("rateker.stream.post").
	directive('rkPost', [
		'postConsts', 
		'Comments',
		function(postConsts, Comments){
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			scope: {
				post: "="
			}, // {} = isolate, true = child, false/undefined = no change
			// controller: function($scope, $element, $attrs, $transclude) {},
			// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
			restrict: 'E', // E = Element, A = Attribute,  C = Class, M = Comment
			// template: '',
			templateUrl: postConsts.baseTempUrl + "post.html",
			replace: true,
			// transclude: true,
			compile: function(tElem, tAttrs) {

				var linkObj =  {
					pre: function(scope, iElem, iAttrs) {
						Comments.get(scope.post.id).then(
							function(data) {
								scope.post.comments = data.comments;
							}
						);

					},
					post: function(scope, iElem, iAttrs) {

					}
				}

				return linkObj;

			},
			link: function($scope, iElm, iAttrs, controller) {
				
			}
		};
	}]);
})();