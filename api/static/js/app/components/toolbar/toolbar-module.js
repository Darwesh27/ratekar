/*!
* I guess this is the start of my files
*
*
*
*/

(function () {
	/*!
	* rkToolbar Module
	*
	* Module for organising components related to the Rateker toolbar
	*/
	angular.module('rateker.rkToolbar', [
		'ngMaterial',
		'rateker.rkToolbar.rkNotifications'
		]).
		constant('toolbarConsts', {

			baseTempUrl: "/static/js/app/components/toolbar/"
		});
})();