(function() {
	angular.module('rateker.rkToolbar.rkNotifications').
	directive('notification', [
		'notificationsService', 
		'notiConsts',
		'Dialog',
		function(notificationsService, notiConsts, Dialog){
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			scope: {
				notification: "=",
				hideDropdown: "&",
			}, // {} = isolate, true = child, false/undefined = no change
			// controller: function($scope, $element, $attrs, $transclude) {},
			// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
			restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
			// template: '',
			templateUrl: notiConsts.baseTempUrl + "/notification.html",
			replace: true,
			// transclude: true,
			// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
			link: function($scope, iElm, iAttrs, controller) {

					var icon = iElm.find('.read-notification-icon');

					iElm.on('hover', function() {
						icon.show();
					});

					iElm.hover(function() {
						icon.toggle();
					})

					var openPost = function(e) {
						// console.log($scope.notification.pid);
						Dialog.post(e, $scope.notification.pid);
					}

					var openPhoto = function(e) {
						Dialog.post(e, $scope.notification.pid);
					}

					var openReview = function(e) {

					}


					var clickActions = [
						openPost,
						openPhoto,
						openReview,
					]

					var types = [
						'Post',
						'Photo',
						'Review'
					]

					var actions = [
						'ratings',
						'comments'
					]

					var reviewActions = [
						'shared',
						'changed',
					]

					var images = [
						'/static/img/notifications/post.png',
						'/static/img/notifications/photo.png',
						'static/img/notifications/review.png',
					]

					var actionImages = [
						'/static/img/notifications/rating.png',
						'/static/img/notifications/comment.png',
					]

					var reviewActionImages = [
						'static/img/notifications/review-new.png',
						'/static/img/notifications/review-old.png',
					]

					var check = function() {
						var a = 1;
						
					}

					// Adding some comment here..

					var postString = function() {
						return "New " + actions[$scope.notification.action - 1] + " on your Post";
					}

					var photoString = function() {
						return "New " + actions[$scope.notification.action - 1] + " on your Photo";
					}

					var reviewString = function() {
						return "Someone " + reviewActions[$scope.notification.action - 1] + " their views about you.";
					}

					var toStrings = [
						postString,
						photoString,
						reviewString,
					]

					$scope.show = function(e) {
						clickActions[$scope.notification.type - 1](e);
						$scope.hideDropdown();
					}
					
					$scope.read = function() {
						notificationsService.read($scope.notification.id);
					}

					$scope.notification.text = "I have to ask you something...";

					$scope.notification.toString = function() {
						return toStrings[$scope.notification.type - 1]();
					}

					$scope.notification.imageUrl = function() {
						return images[$scope.notification.type - 1];
					}

					$scope.notification.actionImageUrl = function() {

						if($scope.notification.type == 3) {
							return reviewActionImages[$scope.notification.action - 1];
						} else {
							return actionImages[$scope.notification.action - 1];
						}
					}
			}
		};
	}]);
})();