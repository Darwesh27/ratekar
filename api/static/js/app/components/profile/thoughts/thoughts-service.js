(function() {
	angular.module('rateker.profile').
	service('Thoughts', [
		'Urls',
		'Errors',
		'ArrangeService',
		function(Urls, Errors, ArrangeService){

			this.initUrl = function() {
				this.url = Urls.thoughts(this.username);
				this.error = "Unable to Fetch thoughts";
			}

			ArrangeService.register(this);

			// Related to stream
			// this.initialized = false;


			// this.previous = null;
			// this.next = null;
			// this.posts = [];
			// var Thoughts = this;


			// var initVars = function() {
			// 	Thoughts.initialized = false;

			// 	Thoughts.previous = null;
			// 	Thoughts.next = null;

			// 	Thoughts.posts = [];
			// }

			// var addToThoughts = function(posts) {
			// 	angular.forEach(posts, function(post) {
			// 		Thoughts.posts.push(post);
			// 	})
			// }

			// var cb = function(data, q) {
			// 	q.resolve(data);
			// }

			// var done = function(data) {

			// 	Thoughts.initialized = true;

			// 	Thoughts.next = data.next;
			// 	Thoughts.previous = data.previous;

			// 	addToThoughts(data.posts);

			// }

			// var nextDone = function(data) {
			// 	Thoughts.next = data.next;

			// 	addToThoughts(data.posts);
			// }

			// var prevDone = function(data) {
			// 	Thoughts.previous = data.previous;

			// 	addToThoughts(data.posts);
			// }

			// var notDone = function(error) {
			// 	// Some error occured while fetching the posts show it.

			// 	console.log(error);
			// }

			// var getPosts = function() {

			// 	var url = Urls.thoughts(Thoughts.username);
			// 	var error = "Can't fetch posts.."

			// 	Fetch.fetch(url, error, cb).then(done, notDone);
			// }

			// var getNext = function() {
			// 	var url = Thoughts.next;

			// 	Fetch.fetch(url, Errors.stream(), cb).then(nextDone, notDone);
			// }

			// var getPrevious = function() {
			// 	var url = Thoughts.previous;

			// 	Fetch.fetch(url, Errors.stream(), cb).then(prevDone, notDone);
			// }

			// this.init = function(username) {
			// 	Thoughts.username = username;
			// 	initVars();
			// 	getPosts();
			// }


			// this.fetchNext = function() {

			// 	if(Thoughts.next && Thoughts.initialized) {
			// 		getNext();
			// 	}
			// }

			// this.fetchPrevious = function() {
			// 	if(Thoughts.previous) {
			// 		getPrevious();
			// 		return true;
			// 	}
			// 	else 
			// 		return false;
			// }

			// this.addNew = function(post) {
			// 	addToThoughts([post]);
			// }

			// this.destroy = function() {
			// 	initVars();
			// }

		}]);
})();