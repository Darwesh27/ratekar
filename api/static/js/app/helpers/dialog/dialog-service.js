(function() {
	angular.module('rateker.helper').
	service('Dialog', [
		'$mdDialog', 
		'helperConsts',
		'http',
		'Urls',
		'$timeout',
		function($mdDialog, helperConsts, http, Urls, $timeout){


			this.login = function(ev) {
				$mdDialog.show({
			      	templateUrl: '/static/js/app/components/auth/login-panel.html',
			      	// targetevent: ev,
			      	controller: 'LoginController',
			    });
			}

			this.signUp = function(ev) {
				$mdDialog.show({
			      	templateUrl: '/static/js/app/components/auth/signup-panel.html',
			      	// targetevent: ev,
			      	controller: 'SignUpController',
			    });
			}

			this.post = function(ev, postId) {

				url = Urls.getPost(postId);

				http.get(url, "").then(
					function(data) {
						$mdDialog.show({
					      	templateUrl: helperConsts.baseTempUrl + "dialog/post.html",
					      	// targetEvent: ev,
					      	controller: 'DialogPostController',
					      	locals: {
						      	post: data.post,
						    }
					    });
					}
				);
			}

			this.review = function(ev, reviewId) {

				url = Urls.getReview(reviewId);

				http.get(url, "").then(
					function(data) {
						$mdDialog.show({
					      	templateUrl: helperConsts.baseTempUrl + "dialog/review.html",
					      	// targetEvent: ev,
					      	controller: 'DialogReviewController',
					      	locals: {
						      	review: data.review,
						    }
					    });
					}
				);
			}

			this.setting = function(ev) {

				url = Urls.getReview(reviewId);

				http.get(url, "").then(
					function(data) {
						$mdDialog.show({
					      	templateUrl: helperConsts.baseTempUrl + "dialog/review.html",
					      	// targetEvent: ev,
					      	controller: 'DialogReviewController',
					      	locals: {
						      	post: data.review,
						    }
					    });
					}
				);
			}
		}
	]).
	controller('DialogPostController', ['$scope', 'post', function($scope, post){
		$scope.post = post;
		$scope.post.thought.text += "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodLLLLLLLLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod";
	}]).
	controller('DialogReviewController', ['$scope', 'review', function($scope, review){
		$scope.review = review;
		// $scope.reviewIdw.text += "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodLLLLLLLLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod";
	}]);
	
})();