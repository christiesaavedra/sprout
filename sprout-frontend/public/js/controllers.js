'use strict';

/* Controllers */

angular.module('sproutApp.controllers', [])
    .controller('BaseController', ['$scope', '$window', 'brand', 'SessionService', function($scope, $window, brand, SessionService) {
        $scope.brand = brand;

        $scope.doLogout = function() {
            SessionService.removeSession();
            $window.location = '/';
        };
    }])
    .controller('HomeController', ['$scope', 'SessionService', function($scope, SessionService) {
        $scope.session = SessionService.getSession();

        $scope.user = {};

        $scope.$on('event:login-confirmed', function() {
            console.log('event has been broadcast to Home Controller');
            $scope.session = SessionService.getSession();
        });
    }])

    .controller('RecipeController', function($scope, SessionService, Restangular) {
        $scope.session = SessionService.getSession();


        Restangular.all('recipes').getList().then(function (data) {
            $scope.recipes = data;
        });
    })

   .controller('EditRecipeController', function($scope, SessionService, Restangular, $routeParams, $location) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).customGET().then(function (data)  {
            $scope.recipe = data;

        })

        $scope.methods = [
            { printed_name: 'Bake', stored_name: 'bake' },
            { printed_name: 'Microwave', stored_name: 'microwave' },
            { printed_name: 'Fry', stored_name: 'fry' },
            { printed_name: 'Dutch Oven', stored_name: 'dutch_oven' }];

        $scope.editRecipe = function() {
            Restangular.one('recipes', $scope.recipeId).customPUT($scope.recipe).then(function (data)  {
                $scope.status = "The recipe was successfully updated!";
                $scope.recipe = data;
                $location.path('/recipes');
            }, function()  {
                $scope.status = "Sorry, this recipe could not be saved"
        })
   }

        $scope.deleteRecipe = function() {
            // put modal confirm box here
            var response = confirm("Are you sure you want to delete this recipe?");

            if (response == true)  {
                Restangular.one('recipes', $scope.recipeId).customDELETE().then(function(data)  {
                   $location.path('/recipes');
                }, function() {
                    $scope.status = "Sorry, this recipe could not be deleted."
                });
            }
        }
    })

   .controller('RecipeDetailsController', function($scope, SessionService, Restangular, $routeParams) {
       $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).customGET().then(function(data)  {
            $scope.recipe = data;

        })
    })

  .controller('AddRecipeController', function($scope, SessionService, Restangular) {
        $scope.session = SessionService.getSession();

        $scope.recipe = {};
        $scope.status = null;
        $scope.methods = [
            { printed_name: 'Bake', stored_name: 'bake' },
            { printed_name: 'Microwave', stored_name: 'microwave' },
            { printed_name: 'Fry', stored_name: 'fry' },
            { printed_name: 'Dutch Oven', stored_name: 'dutch_oven' }];

        $scope.saveNewRecipe = function(){
            Restangular.all('recipes').customPOST($scope.recipe).then(function(){
                $scope.status = 'The recipe was successfully created!';
                $scope.recipe = {};
            }, function(){
                $scope.status = "The recipe couldn't be saved";
        })
       }
    })