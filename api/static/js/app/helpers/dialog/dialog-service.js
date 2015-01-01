(function() {
	angular.module('rateker.helper').
	service('Dialog', [
		'$mdDialog', 
		'helperConsts',
		'http',
		'Urls',
		function($mdDialog, helperConsts, http, Urls){

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
		}
	]).
	controller('DialogPostController', ['$scope', 'post', function($scope, post){
		$scope.post = post;
	}]);
})();