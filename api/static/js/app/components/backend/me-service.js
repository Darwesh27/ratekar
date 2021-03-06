(function() {
	angular.module("rateker.backend").
	service('Me', [
		'$http',
		'Urls',
		'Fetch',
		'$q',
		function($http, Urls, Fetch, $q){

		this.user = null;
		var Me = this;

		this.ready = true;

		this.deffered = $q.defer();


		this.getUser = function() {
			return Me.deffered.promise;
		}

		var getThoughtsRating = function() {
			url = Urls.myThoughtsRating();

			Fetch.fetch(url, '', function(data, q) {q.resolve(data);}).then(
				function(data) {
					Me.user.thoughtsRating = data.rating;
				},
				function(error) {
					console.log(error);
				}
			);

		}

		var initUser = function(user) {

			Me.user = user;
			Me.deffered.resolve(Me.user);
			Me.ready = user.imageUrl != null && user.places;
			// Me.ready = false;
		}


		this.check = function() {
			console.log(this.user);
		}

		this.sessionInit = function(username) {

			Me.deffered = $q.defer();

			$http.get("api/user/" + username + "/profile/", {username: username})
			.success(function(data, status, header, config) {
				initUser(data);
			});
		}

		this.init = function(user) {
			Me.deffered = $q.defer();
			initUser(user);
		}

		this.reload = function() {
			Me.sessionInit(Me.user.username);
		}

		this.destroy = function() {
			this.user = null;
		}
	}]);
})();