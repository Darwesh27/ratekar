(function() {
	angular.module("rateker.profile").
	controller('reviewsController', [
		'$scope', 
		'$timeout',
		'Reviews',
		'username',
		 function($scope, $timeout, Reviews, username){

			Reviews.init(username);

			$scope.reviews = Reviews.items;

			$scope.fetchPrevious = function() {
				Reviews.fetchPrevious();
			}

			$scope.end = {};
			$scope.end.message = "No more Reviews..";
			$scope.end.hasNext = true;

			$scope.$watch(function() {
				return Reviews.previous;
			}, function(value) {
				if(value == null) {
					if(Reviews.items.length > 0) {
						$scope.end.hasNext = false;
					}
				}
				else {
					$scope.end.hasNext = true;
				}
			});


			$scope.abc = [
				{
					text: "Shahid is a great guy.. Very Intelligent.. But gets mad very often.. :P" +
					" Has an awsome sense of humor.." + 
					" is very helping.. and is crazy about adventure.. ",
					date: "2014-07-07",
					liked: true,
				},
				{
					text: "Here is another review from one of your friends.. Its could be a good one" +
					" or a bad one.. If a lot of people are saying the same thing about you that means" +
					" it exists in you.. Some quality or a habit or something.. " ,

					date: "2014-07-19",
					liked: true,
				},
				{
					text: "Shahid is a great guy.. Very Intelligent.. But gets mad very often.. :P" +
					" Has an awsome sense of humor.." + 
					" is very helping.. and is crazy about adventure.. ",
					date: "2014-10-28",
					liked: true,
				},
				{
					text: "Here is another review from one of your friends.. Its could be a good one" +
					" or a bad one.. If a lot of people are saying the same thing about you that means" +
					" it exists in you.. Some quality or a habit or something.. " ,

					date: "2014-10-30",
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


		$timeout(initWookmark, 1000);

		function initWookmark () {
			angular.element(".review-wrapper").wookmark({
				container: angular.element(".reviews"),
				direction: "left",
				offset: 30,
			});
		}
	}])
})();