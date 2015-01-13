(function() {
	/**
	* Welcome Module
	*
	* This module will be encapuslting all the welcome stuff.. THat includes
	  1. iNtro..
	  2. Getting the home and work and showing initial suggestions..
	*/
	angular.module('rateker.welcome', ['ngAnimate']).
	constant('welcomeConsts', {
		baseTempUrl: "/static/js/app/components/welcome/"
	});
})();