
var matApp= angular.module("app", ["ngRoute", "ngMaterial"]);
var BaseTemplateUrl  = "/static/js/app/views/"

matApp.config(["$routeProvider",function($routeProvider){
	$routeProvider.when("/", {
		templateUrl: BaseTemplateUrl + "main.html",
		controller: "MainCtrl"
	})
}])

matApp.controller("MainCtrl", function ($scope) {

});

