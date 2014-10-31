(function() {

	/**
	* rateker.profile Module
	*
	* This module encapsulates the components used in profile
	*/
	angular.module('rateker.profile', ['ngMaterial', 'rateker.stream.post']).
		constant('profileConsts', {
			baseTempUrl : "/static/js/app/components/profile/",
		});
})();