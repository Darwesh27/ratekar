(function() {
	angular.module('rateker.stream').
	service('Stream', [
		'Fetch', 
		'Urls', 
		'Errors', 
		'$timeout',
		function(Fetch, Urls, Errors, $timeout){


			// Related to stream
			this.initialized = false;


			this.previous = null;
			this.next = null;
			this.posts = [];
			var Stream = this;


			var initVars = function() {
				this.initialized = false;

				this.previous = null;
				this.next = null;
				this.befNext = null;
				this.befPrev = null;
				this.posts = [];
			}

			var addToStream = function(posts) {
				angular.forEach(posts, function(post) {
					Stream.posts.push(post);
				})
			}

			var cb = function(data, q) {
				q.resolve(data);
			}

			var done = function(data) {

				Stream.initialized = true;

				Stream.next = data.next;
				Stream.previous = data.previous;

				addToStream(data.posts);

			}

			var nextDone = function(data) {
				Stream.next = data.next;

				addToStream(data.posts);
			}

			var prevDone = function(data) {
				Stream.previous = data.previous;

				addToStream(data.posts);
			}

			var notDone = function(error) {
				// Some error occured while fetching the posts show it.

				console.log(error);
			}

			var getPosts = function() {

				var url = Urls.stream();
				var error = Errors.stream();

				Fetch.fetch(url, error, cb).then(done, notDone);
			}

			var getNext = function() {
				var url = Stream.next;

				Fetch.fetch(url, Errors.stream(), cb).then(nextDone, notDone);
			}

			var getPrevious = function() {
				var url = Stream.previous; 

				Fetch.fetch(url, Errors.stream(), cb).then(prevDone, notDone);
			}

			this.init = function() {
				initVars();
				getPosts();
			}


			this.fetchNext = function() {

				if(Stream.next && Stream.initialized) {
					getNext();
				}
			}

			this.fetchPrevious = function() {
				if(Stream.previous) {
					getPrevious();
					return true;
				}
				else 
					return false;
			}

			this.addNew = function(post) {
				addToStream([post]);
			}

			this.destroy = function() {
				initVars();
			}
		}]);
})();