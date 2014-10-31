(function  () {

	var fuckService =  function() { 
		return {
			get: function  () {
				// body...
				return [
					{
						id : 1,
						author: {
							name: 'Malik Junaid',
							imageUrl: '/static/img/mj2.jpg',
							url: '/#/malik.junaid'
						},
						time: 'Today',
						rating: 5.6,
						myRating: 4,
						content: {
							text: 'hello this is my very first post' + 
							'some random text' + 
							'some random text' + 
							'some random text' + 
							'some random text' + 
							'some random text' + 
							'some random text' + 
							'some random text' + 
							'some random text'
						},

						comments : [
							{
								text: "This is a nice comment"
							},
							{
								text: "This is another nice comment"
							},
							{
								text: "This is yet another nice comment" +
								" Some random text " + 
								" Some random text " + 
								" Some random text " + 
								" Some random text " + 
								" Some random text " + 
								" Some random text " + 
								" Some random text " + 
								" Some random text " + 
								" Some random text " + 
								" Some random text " + 
								" Some random text " + 
								" Some random text "
							},
							{
								text: "This is a bad comment"
							},
							{
								text: "This is another bad comment"
							},

						]
					},
				]
			}
		}
	};
	
	angular.module("rateker.stream").
	factory('fuck', fuckService).
	controller('StreamCtrl', ['$scope', '$routeParams', 'fuck', function($scope, $routeParams, fuck){
		$scope.posts = fuck.get();
	}]);
})();