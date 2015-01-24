(function() {
	angular.module('rateker.welcome').
	controller('WelcomeController', [
		'$scope', 
		'Urls', 
		'$http', 
		'welcomeConsts',
		'Me',
		'Welcome',
		'$location',
		function($scope, Urls, $http, welcomeConsts, Me, Welcome, $location){


			$scope.user = Me.user;
			
			var baseUrl = welcomeConsts.baseTempUrl;

			$scope.intro = {};

			$scope.intro.step = 0;

			$scope.intro.urls = [
				baseUrl + 'intro-01.html',
				baseUrl + 'intro-02.html',
				baseUrl + 'intro-03.html',
				baseUrl + 'intro-04.html',
			]

			$scope.intro.setPage = function(pageNo) {
				$scope.intro.step = pageNo;
			}

			$scope.intro.next = function() {

				if($scope.intro.step < 3) {
					$scope.intro.step += 1;
				}
				else {
					// The intro is complete
					$scope.welcome.next();
				}
			}


			$scope.welcome = {

			};

			$scope.welcome.step = 0;

			$scope.welcome.urls = [
				baseUrl + 'intro.html',
				baseUrl + 'photo.html',
				baseUrl + 'work.html',
				baseUrl + 'suggestions.html',
			]

			$scope.welcome.buttonTexts = [
				"Skip intro..",
				"Next",
				"Finish"
			]

			$scope.welcome.next = function() {

				console.log($scope.welcome.step);

				if($scope.welcome.step == 0) {

					if(Me.user.imageUrl) {
						$scope.welcome.step = 1;
						$scope.welcome.next();
					}
					else {
						$scope.welcome.step = 1;
					}

				}
				else if($scope.welcome.step == 1) {

					if($scope.photo.uploaded || Me.user.imageUrl) {
						if(Me.user.places) {
							$scope.welcome.step = 2;
							$scope.welcome.next();
						}
						else {
							$scope.welcome.step = 2;
						}
					}

					// Photo is not uploaded so Shouldn't do anything..

				}
				else if($scope.welcome.step == 2) {

					if(!$scope.address.updated()) {
						// Do nothing yet..
						if(Me.user.places) {
							$scope.welcome.step = 3;
						}
					}
					else {
						// Set places 
						$scope.address.update().then(
							function(data) {
								Me.reload();
								$scope.welcome.step += 1;
							},
							function(error) {
								// Show an error
							}
						);
					}
				}
				else if($scope.welcome.step == 3) {
					console.log(Me.user.username);
					$location.path('/' + Me.user.username);
				}
				else {
					$scope.welcome.step += 1;
				}
			}

			$scope.$watch(
				function() {
					return $scope.photo.data;
				},
				function(val) {
					if(val) {
						$scope.photo.upload();
					}
				}
			);

			$scope.photo = {
				data : null,
				uploaded: false,
				url: null,
				upload: function() {

					if($scope.photo.data) {
						fd = new FormData();
						fd.append('picture', $scope.photo.data);

						console.log(fd);

						var url = "/api/upload/profile/";

						$http.post(url, fd, {
				            transformRequest: angular.identity,
				            headers: {'Content-Type': undefined}
				        })
				        .success(function(data){
				        	$scope.photo.uploaded = true;
				        	$scope.photo.message = "Click to change.";
				        	$scope.photo.url = data.url;
				        	Me.reload();
				        })
				        .error(function(){
				        	$scope.photo.message = "Error";
				        });
					}
				}
			}

			$scope.address = {
				places: [
					{
						name: "",
						suggestions: null,
					},
					{
						name: "",
						suggestions: null,
					},
					{
						name: "",
						suggestions: null,
					},
				],

				update: function() {
					return Welcome.updatePlaces($scope.address.places);
				},
				updated : function() {
					var places = $scope.address.places;
					return places[0].name.length >= 3 && places[1].name.length >= 3 && places[2].name.length >= 3;
				},
				init: function() {

					angular.forEach($scope.address.places, function(place) {

					})
				},

			}

			$scope.address.init();

















		
	}]);
})();