(function() {

	angular.module("rateker.stream.post").
	directive('newComment', [
		'postConsts', 
		'Comment',
		'Me', 
		function(postConsts, Comment, Me){
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			scope: {
				post: "=",
			}, // {} = isolate, true = child, false/undefined = no change
			// controller: function($scope, $element, $attrs, $transclude) {},
			require: '^rkPost', // Array = multiple requires, ? = optional, ^ = check parent elements
			restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
			// template: '',
			templateUrl: postConsts.baseTempUrl + "new-comment/new-comment.html",
			replace: true,
			// transclude: true,
			// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
			link: function($scope, iElm, iAttrs, postCont) {


				$scope.me = Me.user;

				$scope.newCom = "";

				var addComment = function() {
					Comment.add($scope.post.id, $scope.newCom).then(
						function(data) {
							// $scope.post.comments.push(data.comment);
							postCont.fetchNextCom();
							$scope.newCom = "";
						}, 
						function(error) {

						}
					);
				}

				var isOk = function() {
					return $scope.newCom != null && $scope.newCom != "";

				}


				iElm.find('input').keypress(function(e) {
					var code = (e.keyCode)?e.keyCode:e.which;

					if(code == 13) {
						console.log("Enter pressed");
						console.log($scope.newCom);
						if(isOk()) {
							console.log("isOk");
							addComment();
						}
					}

				})
			}
		};
	}]);
})();