// SOURCE: http://codepen.io/Thibka/pen/mWGxNj
var app = angular.module('baseApp',['ui.bootstrap']);
app.controller('mainController', function($scope, $http, $uibModal){
  console.log("Connected");

  $scope.deletePost = function(){
    console.log("delete Post");
    return confirm("Are you sure to delete Post!!!");
  }
  $scope.show = false;
  $scope.showlist = function(){
    console.log("show Post list");
    $scope.show = true;
  }

});
