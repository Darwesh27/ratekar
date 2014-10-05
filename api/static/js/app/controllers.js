var aMailServices = angular.module('AMail', ['ngRoute']);
var BaseTemplateUrl = 'static/js/app/views/';


function ListController($scope) {
	$scope.messages = messages;
}

function DetailController($scope, $routeParams) {
	$scope.message = messages[$routeParams.id];
}
	
aMailServices.controller('ListController', ['$scope', ListController]);
aMailServices.controller('DetailController', ['$scope', '$routeParam', DetailController]);

aMailServices.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
    when('/', {
//        controller: ListController,
        templateUrl: BaseTemplateUrl + 'list.html'
    }). 
    when('/view/:id', {
        controller: DetailController,
        templateUrl: BaseTemplateUrl + 'detail.html'
    }). 
    otherwise({
        redirectTo: '/'	
    });
}]);




messages = [
	{
		id: 0, sender: 'jean@somecompany.com', subject: 'Hi there, old friend',
		date: 'Dec 7, 2013 12:32:00', recipients: ['greg@somecompany.com'],
		message: 'Hey, we should get together for lunch sometime and catch up.'
		+'There are many things we should collaborate on this year.'
    },
	{
		id: 1, sender: 'maria@somecompany.com',
		subject: 'Where did you leave my laptop?',
		date: 'Dec 7, 2013 8:15:12', recipients: ['greg@somecompany.com'],
    }, 
	{
		id: 2, sender: 'bill@somecompany.com', subject: 'Lost python',
		date: 'Dec 6, 2013 20:35:02', recipients: ['greg@somecompany.com'],
		message: "Nobody panic, but my pet python is missing from her cage."
		+"She doesn't move too fast, so just call me if you see her."
    }
];




            

