(function() {
	angular.module('rateker.backend').
	service('notificationsService', ['$http', function($http){
		this.notifications = {
			count : 0,
			items : []
		}

		this.friendRequests = {
			count : 0,
			items : []
		}

		this.messages = {
			count : 0,
			items : []
		}
	}]);
})();