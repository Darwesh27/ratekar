(function  () {
	
	angular.module("rateker.stream.post").
	directive('rkPost', [
		'postConsts', 
		'Comments',
		'$interval',
		'$timeout',
		'Post',
		function(postConsts, Comments, $interval, $timeout, Post){
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			scope: {
				post: "="
			}, // {} = isolate, true = child, false/undefined = no change
			controller: ['$scope', '$element', '$attrs', '$transclude', function($scope, $element, $attrs, $transclude) {

				this.fetchNextCom = function() {
					$scope.fetchNextCom();
				}

			}],
			// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
			restrict: 'E', // E = Element, A = Attribute,  C = Class, M = Comment
			// template: '',
			templateUrl: postConsts.baseTempUrl + "post.html",
			replace: true,
			// transclude: true,
			compile: function(tElem, tAttrs) {

				var linkObj =  {


					pre: function(scope, iElem, iAttrs) {

						scope.prevComments = null;
						scope.nextComments = null;


						var addToComments = function(comments) {
							angular.forEach(comments, function(comment) {
								scope.post.comments.push(comment);
							})
						}

						// Fetch the comments for the first time
						Comments.get(scope.post.id).then(
							function(data) {
								scope.post.comments = data.comments;
								scope.nextComments = data.next;
								scope.previousComments = data.previous;
								scope.befNext = data.befNext;
								scope.befPrev = data.befPrev;
							}
						);

						scope.fetchNextCom = function() {
							Comments.next(scope.post.id, scope.nextComments, scope.befNext).then(
								function(data) {
									addToComments(data.comments);
									scope.nextComments = data.next;
									scope.befNext = data.befNext;
								}
							);
						}

						scope.fetchPrevCom = function() {
							Comments.previous(scope.post.id, scope.previousComments, scope.befPrev).then(
								function(data) {
									addToComments(data.comments);
									scope.previousComments = data.previous;
									scope.befPrev = data.befPrev;
								}
							);
						}


						var fetchingComments = $interval(function() {
							if(scope.nextComments) {
								scope.fetchNextCom();
							}
						}, 5000);


						scope.$on("$destroy" , function(e) {
							$interval.cancel(fetchingComments);
						});


					},
					post: function(scope, iElem, iAttrs) {

						// Post rating
						scope.$watch(
							function() {
								return scope.post.rating.my;
							}, 
							function(value, old) {

								if(old != value) {
									Post.rate(scope.post.id, value).then(
										function(data) {
											scope.post.rating = null;
											scope.post.rating = angular.copy(data.rating);
										},
										function(error) {

										}
									);
								}
							}
						);

					}
				}

				return linkObj;

			},
			link: function($scope, iElm, iAttrs, controller) {
				
			}
		};
	}]);
})();