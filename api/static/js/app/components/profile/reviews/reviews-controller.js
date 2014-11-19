(function() {
	angular.module("rateker.profile").
	controller('reviewsController', [
		'$scope', 
		'$timeout',
		'data',
		 function($scope, $timeout, data){
			console.log("Reviews" + data);
		 	$scope.data = data;
		$scope.reviews = [
			{
				text: "Hello this is a review. And it is a very good review. It is a very assome " +
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" ,
				date: "2014-10-28",
				liked: true,
			},
			{
				text: "Hello this is a review. And it is a very good review. It is a very assome " +
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" +
				" some random text" + 
				" some random text" + 
				" some random text" ,

				date: "2014-10-28",
				liked: true,
			},
			{
				text: "Hello this is a review. And it is a very good review. It is a very assome " +
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" ,

				liked: true,
				date: "2014-10-28"
			},
			{
				text: "Hello this is a review. And it is a very good review. It is a very assome " +
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" ,
				liked: true,
				date: "2014-10-28"
			},
			{
				text: "Hello this is a review. And it is a very good review. It is a very assome " +
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" ,

				liked: true,
				date: "2014-10-28"
			},
			{
				text: "Hello this is a review. And it is a very good review. It is a very assome " +
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" + 
				" some random text" ,

				liked: false,
				date: "2014-10-28"
			},
		];


		$timeout(initWookmark, 100);

		function initWookmark () {
			angular.element(".review-wrapper").wookmark({
				container: angular.element(".reviews"),
				direction: "left",
				offset: 30,
			});
		}
	}])
})();