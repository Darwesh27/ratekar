(function() {
	angular.module("rateker.right-pane").
	filter('adjustLength', function(){
		return function(input, length) {

				if(input.length < length) {
					return input;
				}
				else {
					return input.substr(0, length-3) + "...";
				}
			};
	})
})();