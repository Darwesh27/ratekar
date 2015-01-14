(function() {
	angular.module('rateker.profile').
	service('ArrangeService', [
		'Fetch',
		'Urls',
		'Errors',
		'http',
		function(Fetch, Urls, Errors, http){


			this.register = function(Caller) {

				Caller.initialized = false;

				Caller.previous = null;
				Caller.next = null;
				Caller.items = [];
				Caller.fetching = false;

				Caller.initVars = function() {

					Caller.initialized = false;

					Caller.previous = null;
					Caller.next = null;

					while(Caller.items.length) {
						Caller.items.pop();
					}

					Caller.initUrl();
				}

				Caller.addToItems = function(items) {
					angular.forEach(items, function(item) {
						Caller.items.push(item);
					})
				}

				var cb = function(data, q) {
					q.resolve(data);
				}

				Caller.done = function(data) {

					Caller.initialized = true;

					Caller.next = data.next;
					Caller.previous = data.previous;

					Caller.addToItems(data.items);

					Caller.fetching = false;
				}

				Caller.nextDone = function(data) {
					Caller.next = data.next;

					Caller.addToItems(data.items);

					Caller.fetching = false;
				}

				Caller.prevDone = function(data) {
					Caller.previous = data.previous;

					Caller.addToItems(data.items);

					Caller.fetching = false;
				}

				Caller.notDone = function(error) {
					// Some error occured while fetching the posts show it.

					Caller.fetching = false;
					console.log(error);
				}

				Caller.getItems = function() {

					var url = Caller.url;
					var error = Caller.error;

					http.get(url, error).then(Caller.done, Caller.notDone);
				}

				Caller.getNext = function() {
					var url = Caller.next;

					http.get(url, Caller.error).then(Caller.nextDone, Caller.notDone);
				}

				Caller.getPrevious = function() {
					var url = Caller.previous;
					var error = Caller.error;

					http.get(url, error).then(Caller.prevDone, Caller.notDone);
				}

				Caller.init = function(username) {
					Caller.username = username;
					Caller.initVars();
					Caller.getItems();
				}


				Caller.fetchNext = function() {

					if(Caller.next && Caller.initialized && !Caller.fetching) {
						Caller.fetching = true;
						Caller.getNext();
					}
				}

				Caller.fetchPrevious = function() {
					if(Caller.previous && !Caller.fetching) {
						Caller.fetching = true;
						Caller.getPrevious();
						return true;
					}
					else 
						return false;
				}

				Caller.addNew = function(item) {
					Caller.addToItems([item]);
				}

				Caller.destroy = function() {
					Caller.initVars();
				}

			}

		}]);
})();