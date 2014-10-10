(function  () {
	/**
	* Stream Module
	*
	* This is wrapper for components related to the Streaam 
	*/
	angular.module('rateker.stream', ['ngMaterial', 'rateker.stream.post']).
		constant('streamConsts', {
			baseTempUrl: "/static/js/app/components/stream/"
		});
})();