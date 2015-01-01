(function() {
	angular.module('rateker.backend').
	service('notificationsService', [
		'http', 
		'Urls',
		'$interval',
		'$rootScope',
		function(http, Urls, $interval, $rootScope){

			var Noti = this;

			var oldRequests = [];

			var initVars = function() {

				Noti.notifications = {
					count : 0,
					items : []
				}

				Noti.friendRequests = {
					count : 0,
					items : [],
					old: []
				}

				Noti.messages = {
					count : 0,
					items : []
				}


			}




			this.getMessages = function() {

			}

			this.getRequests = function() {
				url = Urls.friendRequests();

				http.post(url, {exclude: Noti.friendRequests.old}, '').then(
					function(data) {

						angular.forEach(data.requests, function(request) {
							Noti.friendRequests.old.push(request.username);

							Noti.friendRequests.items.push(request);
						});

						Noti.friendRequests.count += data.requests.length;

					}, 
					function(error) {

					}
				);
			}

			this.getNotifications = function() {
				
			}

			this.init = function() {

				initVars();

				Noti.getNotifications();
				Noti.getRequests();
				Noti.getMessages();

				$interval(function() {
					Noti.getRequests();
				}, 60000);
			}

	}]);
})();