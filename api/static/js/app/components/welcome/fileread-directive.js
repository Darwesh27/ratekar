(function() {
	angular.module('rateker.welcome').
	directive('fileread', ['$parse', function($parse){
		// Runs during compile
		return {
			// name: '',
			// priority: 1,
			// terminal: true,
			// scope: {
			// 	fileread: "="
			// }, // {} = isolate, true = child, false/undefined = no change
			// controller: function($scope, $element, $attrs, $transclude) {},
			// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
			restrict: 'A', // E = Element, A = Attribute, C = Class, M = Comment
			// template: '',
			// templateUrl: '',
			// replace: true,
			// transclude: true,
			// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
			link: function($scope, iElm, iAttrs, controller) {


				var model = $parse(iAttrs.fileread);
	            var modelSetter = model.assign;
	            
	            iElm.bind('change', function(){
	                $scope.$apply(function(){
	                    modelSetter($scope, iElm[0].files[0]);


	                    //startupload 
	                });
	            });
				
			}
		};
	}]);
})();