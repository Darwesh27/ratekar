(function() {
	angular.module('rateker.helper')
	.directive('friendStatusButton', [
		'helperConsts', 
		'Urls', 
		'Fetch', 
		'http',
		function(helperConsts, Urls, Fetch, http){
			// Runs during compile
			return {
				// name: '',
				// priority: 1,
				// terminal: true,
				scope: {
					username: "@",
					hurrah: "&",
				}, // {} = isolate, true = child, false/undefined = no change
				// controller: function($scope, $element, $attrs, $transclude) {},
				// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
				restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
				// template: '',
				templateUrl: helperConsts.baseTempUrl + 'friend-status-button/friend-status-button.html',
				// replace: true,
				// transclude: true,
				compile: function(tElement, tAttrs){
					return {
						pre: function($scope, iElm, iAttrs, controller) {

							iElm.on('click', function() {

								url = Urls.friendStatus($scope.username);

								Fetch.fetch(url, '', function(data,q) {q.resolve(data)}).then(
									function(data) {
										initScope(data);
										afterLoad();
									}
								);
							});

							var circles = [
								{
									name: "Family",
									exists : false,
								},
								{
									name: "Close Friends",
									exists : false,
								},
								{
									name: "Friends",
									exists : false,
								},
								{
									name: "Acuantance",
									exists : false,
								},
							]


							// Initialize the $scope
							var initScope = function(data) {

								$scope.friendship = data.friendship;
								$scope.circles = circles;

								if($scope.friendship.status == 3) {
									$scope.circles[$scope.friendship.circle].exists = true;
								}
								else if($scope.friendship.me) {
									iElm.hide();
								}

								var buttonTexts = [
									"Add Friend",
									"Respond to Friend Request",
									"Friend Request Sent",
									"Friends"
								]

								var cancelTexts = [
									"",
									"Not Now",
									"Cancel Request",
									"unfriend"
								]


								$scope.buttonText = buttonTexts[$scope.friendship.status];

								$scope.cancelText = cancelTexts[$scope.friendship.status];

							}


							// initializes the code
							var initButton = function() {
								url = Urls.friendStatus($scope.username);

								Fetch.fetch(url, '', function(data,q) {q.resolve(data)}).then(
									function(data) {
										initScope(data);
										afterLoad();
									}
								);


								$scope.unfriend = function() {
									url = Urls.unfriend();

									http.post(url, {user: $scope.username}, "Can't unfriend")
									.then(
										function(data) {
											initScope(data);
											$scope.hurrah();
											// window.reload();
										},
										function(error) {

										}
									);
								}
							}


							// Backend for changing the circle..
							var friendCircleAction = function(circleNo) {
								url = Urls.changeCircle($scope.username);

								result = false

								return http.post(url, {circle: circleNo}, "").then(
									function(data) {
										// Circle changed at the backend..
										return true;
									},
									function(error) {
										// Circle Not changed 
										return false;
									}
								);

							}

							var notFriendCircleAction = function(circleNo) {
								url = Urls.addFriend();

								data = {
									user: $scope.username,
									circle: circleNo
								}

								return http.post(url,data,"Unable to add Friend").then(
									function(data) {
										initScope(data);
									},
									function(error) {

									}
								);
							}



							var afterLoad = function() {
								
								var circleAction = [
									notFriendCircleAction,
									notFriendCircleAction,
									notFriendCircleAction,
									friendCircleAction
								]

								angular.forEach($scope.circles, function(circle, circleNo) {

									$scope.$watch(function() {
										return circle.exists;
									},
									function(newVal, oldVal) {

										if(newVal != oldVal && newVal == true) {
											circleAction[$scope.friendship.status](circleNo).then(
												function() {
													angular.forEach($scope.circles, function(c) {
														c.exists = false;
													});

													circle.exists = true;

													$scope.hurrah();

												},
												function() {
													circle.exists = false;
												}
											);
										}
									});
								});
							}


							initButton();

						},
						post: function($scope, iElm, iAttrs, controller) {


						}
					}
				},
			};
		}]);
})();