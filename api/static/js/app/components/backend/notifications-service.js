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
					dict: {},
					items : [],
					old: {},
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

			var arrangeNotifications = function() {
				Noti.notifications.count = Object.keys(Noti.notifications.dict).length
				Noti.notifications.items.splice(0, Noti.notifications.items.length);

				for(key in Noti.notifications.dict) {
					Noti.notifications.items.push(Noti.notifications.dict[key]);
				}
			}

			var showNotifications = function(data) {
					angular.forEach(data.notifications, function(notification) {

						if(Noti.notifications.dict.hasOwnProperty(notification.id)) {
							Noti.notifications.dict[notification.id].time = notification.time;
						}
						else {
							Noti.notifications.dict[notification.id] = notification;
							Noti.notifications.old[notification.id] = notification.id;
						}

					})

					arrangeNotifications();
			}

			this.getNotifications = function() {

				url = Urls.notifications();

				http.get(url, '').then(showNotifications);
				
			}

			this.updateNotifications = function() {
				url = Urls.updateNotifications();

				http.get(url, '').then(showNotifications);
			}



			this.read = function(nid) {

				url = Urls.readNotification();

				data = {
					nid: nid,
				}

				http.post(url, data, '').then(
					function() {
						delete Noti.notifications.dict[nid];
						delete Noti.notifications.old[nid];
						arrangeNotifications();
					}
				);
			}


			this.readAll = function() {
				url = Urls.readAllNotifications();

				data = {
					nids: Object.keys(Noti.notifications.old),
				}

				http.post(url, data, '').then(
					function() {
						for(key in Noti.notifications.dict) {
							delete Noti.notifications.dict[key]
							delete Noti.notifications.old[key]
						}

						arrangeNotifications();
					}
				);
			}

			this.init = function() {

				initVars();

				Noti.getNotifications();
				Noti.getRequests();
				Noti.getMessages();


				var updateNotis = $interval(function(){
					Noti.updateNotifications();
				}, 10000);

				var updatingRequests = $interval(function() {
					Noti.getRequests();
				}, 60000);


				$rootScope.$on('logOut', function() {
					$interval.cancel(updatingRequests);
					$interval.cancel(updateNotis);
				})
			}

	}]);
})();