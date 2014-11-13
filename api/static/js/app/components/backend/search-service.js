(function() {
	angular.module("rateker.backend").
	service('searchService', ['$http', function($http){
		this.search = {
			text: "",
			items: []
		}
	}]);
})();