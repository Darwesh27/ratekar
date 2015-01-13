(function() {
	angular.module('rateker.welcome').
	service('Welcome', [
		'http', 
		'Urls', 
		function(http, Urls){


			this.updatePlaces = function(places) {
				var data = {};
				data.places = []

				angular.forEach(places, function(place) {
					data.places.push(place.name);
				})

				url = Urls.updatePlaces();

				console.log(data.places);

				return http.post(url, data, '');
			}
		
			this.suggestPlaces = function(text) {


				url = Urls.suggestPlaces();

				data = {
					text: text
				}

				return http.post(url, data, '');

				// http.post(url, data, '').then(
				// 	function(data) {
				// 		console.log(place.suggestions);
				// 		place.suggestions = data.places;
				// 	},
				// 	function(error) {
				// 		place.suggestions = [];
				// 	}
				// );
			}
	}])
})();