(function  () {
	
	/**
	* rateker Module
	*
	* The main module that will basically be acting as the namespace
	*/

	'use strict';

	angular.module('rateker', [
		'rateker.rkToolbar', 
		'rateker.stream',
		'rateker.profile',
		'rateker.backend',
		'ngRoute',
		'ui.router',
		'ngCookies',
		'angular-loading-bar'

	]).
	run(['$http', '$cookies', '$cookieStore', 'Auth' , function($http, $cookies, $cookieStore, Auth) {
		$http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
	}]).
	config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
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
						console.log("G G ");
						// return Profile.check();
						return Profile.init($stateParams.username);
						// return $http.get('api/user/' + $stateParams.username + '/profile/');
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
			})
			.state('profile.profile.reviews', {
				url: '/reviews',
				templateUrl: "static/js/app/components/profile/reviews/reviews.html",
				controller: 'reviewsController',
			})
			.state('profile.profile.nicks', {
				url: '/nicks',
				templateUrl: "static/js/app/components/profile/nicks/nicks.html",
				controller: 'nicksController'
			})
			.state('profile.timeline.thoughts', {
				url: '',
				templateUrl: "static/js/app/components/profile/thoughts/thoughts.html",
			})
			.state('profile.timeline.photos', {
				url: '/photos',
				templateUrl: "static/js/app/components/profile/photos/photos.html",
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
