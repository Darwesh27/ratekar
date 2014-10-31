(function  () {
	
	/**
	* rateker Module
	*
	* The main module that will basically be acting as the namespace
	*/
	angular.module('rateker', [
		'rateker.rkToolbar', 
		'rateker.stream',
		'rateker.profile',
		'rateker.backend',
		'ngRoute',
		'ui.router'

	]).
	config(['$stateProvider', '$urlRouterProvider' ,function($stateProvider, $urlRouterProvider) {
		$urlRouterProvider.otherwise("/");

		$stateProvider
			.state('stream', {
				url: "/",
				templateUrl: "/static/js/app/components/stream/stream.html",
			})
			.state('profile', {
				url: "/:username",
				templateUrl: "static/js/app/components/profile/profile.html",
				abstract: true,
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

	controller('TestCtrl', ['$scope', 'fuck', function($scope, fuck){
		$scope.checks = fuck.get();

		$scope.noti = $scope.checks[0].myRating;
	}]);
})();
