(function  () {

	var Posts = [
		{
			id : 1,
			author: {
				name: 'Malik Junaid',
				image_url: '/static/img/thumb-up/png/36/thumb-up.png',
				url: "/malik.junaid"
			},
			time: 'today',
			content: {
				text: 'hello this is my very first post'
			}
		},
		{
			id : 2,
			author: {
				name: 'Suleman Farooq',
				image_url: '/static/img/thumb-up/png/36/thumb-up.png',
				url: "/malik.junaid"
			},
			time: 'today',
			content: {
				text: 'Hello this is my first content for today too..'
			}
		},
	]
	
	angular.module("rateker.stream.post").
	factory('postsService', ['', function(){
		return {
			get: function  () {
				return Posts;
			}
		}
	}]);
})();