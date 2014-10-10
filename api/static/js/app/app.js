(function  () {
	
	/**
	* rateker Module
	*
	* The main module that will basically be acting as the namespace
	*/
	angular.module('rateker', [
		'rateker.rkToolbar', 
		'rateker.stream',
		'ngRoute'

	]).
	config(['$routeProvider',function($routeProvider) {
		$routeProvider.when('/',{
			templateUrl: "/static/js/app/views/main.html",

		});

	}]).

	controller('TestCtrl', ['$scope', function($scope){
		$scope.noti = 1;
	}])
})();
