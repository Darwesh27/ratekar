(function  () {
	
	/**
	* rateker Module
	*
	* The main module that will basically be acting as the namespace
	*/

	'use strict';
	var app = angular.module('rateker', [
		'rateker.rkToolbar', 
		'rateker.stream',
		'rateker.profile',
		'rateker.backend',
		'rateker.right-pane',
		'rateker.dropdown',
		'rateker.auth',
		'rateker.dropdown',
		'rateker.helper',
		'ngRoute',
		'ui.router',
		'ngCookies',
		'angular-loading-bar',
		'monospaced.elastic',

	]);

	var fetchData = function() {
		var initInjector = angular.injector(["ng"]);
		var $q = initInjector.get("$q");
		var $timeout = initInjector.get("$timeout");


		var d = $q.defer();



		$timeout(function() {
			d.resolve();
		}, 200);

		return d.promise;
	}

	var bootstrapApp = function() {
		angular.element(document).ready(function() {
			angular.bootstrap(document, ["rateker"]);
		});
	}

	fetchData().then(bootstrapApp);

	app.
	run([
		'$http', 
		'$cookies', 
		'$cookieStore', 
		'Auth', 
		function($http, $cookies, $cookieStore, Auth) {
			$http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
	}]).
	config([
		'$stateProvider', 
		'$urlRouterProvider', 
		'$httpProvider',
		function($stateProvider, $urlRouterProvider, $httpProvider) {
			
			$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

			console.log("Main config");
			$urlRouterProvider.otherwise("/");

			$stateProvider
				.state('auth', {
					url: "/enter",
					templateUrl: "static/js/app/components/auth/enter.html",
				})
				.state('stream', {
					url: "/",
					templateUrl: "/static/js/app/components/stream/stream.html",
				})
				.state('profile', {
					url: "/:username",
					templateUrl: "static/js/app/components/profile/profile.html",
					resolve: {
						Profile: 'Profile',
						profile: function($stateParams, Profile, $http) {
							return Profile.init($stateParams.username);
						}
					},
					abstract: true,
					controller: 'profileController'
				})
				.state('profile.timeline', {
					url: '',
					templateUrl: "static/js/app/components/profile/timeline.html",
					abstract: true,
				})
				.state('profile.profile', {
					url: '',
					templateUrl: "static/js/app/components/profile/profile-content.html",
					abstract: true,
				})
				.state('profile.profile.feedbacks', {
					url: '/feedbacks',
					templateUrl: "static/js/app/components/profile/feedbacks/feedbacks.html",
					controller: 'feedbacksController',
					resolve: {
						username: function($stateParams) {
							return $stateParams.username;
						}
					}
				})
				.state('profile.profile.reviews', {
					url: '/reviews',
					templateUrl: "static/js/app/components/profile/reviews/reviews.html",
					controller: 'reviewsController',
					resolve: {
						username: function($stateParams) {
							return $stateParams.username;
						}
					}
				})
				.state('profile.profile.nicks', {
					url: '/nicks',
					templateUrl: "static/js/app/components/profile/nicks/nicks.html",
					controller: 'nicksController',
					resolve: {
						username: function($stateParams) {
							return $stateParams.username;
						}
					}
				})
				.state('profile.timeline.thoughts', {
					url: '',
					templateUrl: "static/js/app/components/profile/thoughts/thoughts.html",
					controller: 'thoughtsController',
					resolve: {
						username: function($stateParams) {
							return $stateParams.username;
						}
					}
				})
				.state('profile.timeline.photos', {
					url: '/photos',
					templateUrl: "static/js/app/components/profile/photos/photos.html",
					controller: 'photosController',
					resolve: {
						data: function(Photos) {
							return Photos.get();
						}
					}
				})

		// $routeProvider.when('/',{
		// 	templateUrl: "/static/js/app/views/main.html",
		// }).
		// when('/:username', {
		// 	templateUrl: "/static/js/app/components/profile/profile.html",
		// })

	}]).
	controller('TestCtrl', ['$scope', 'searchService', function($scope, searchService){

	}]);




})();
