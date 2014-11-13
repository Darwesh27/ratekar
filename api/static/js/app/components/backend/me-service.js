(function() {
	angular.module("rateker.backend").
	service('Me', ['$http', function($http){

		this.user = null;
		var Me = this;



		var initUser = function(data) {
			Me.user = data;
		}


		this.check = function() {
			console.log(this.user);
		}


		this.getUser = function() {
			return this.user;
		}

		this.sessionInit = function(username) {


			$http.get("api/user/" + username + "/profile/", {username: username})
			.success(function(data, status, header, config) {
				initUser(data);
			});
		}

		this.init = function(user) {
			initUser(user);
		}

		this.destroy = function() {
			this.user = null;
		}
	}]);
})();