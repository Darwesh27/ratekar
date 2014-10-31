(function() {

	angular.module("rateker.profile").
	controller('feedbacksController', ['$scope', function($scope){
		$scope.feedbacks = [
			{
				trait: "Adventerous",
				rating: 8.6,
			},
			{
				trait: "Cultured",
				rating: 7.2,
			},
			{
				trait: "Dependable",
				rating: 5.6,
			},
			{
				trait: "Fair",
				rating: 9.5,
			},
			{
				trait: "Fearless",
				rating: 6.1,
			},
			{
				trait: "Lazy",
				rating: 8.9,
			},
			{
				trait: "Picky",
				rating: 6.9,
			},
			{
				trait: "Moody",
				rating: 7.7,
			},
		];
	}])							
})();