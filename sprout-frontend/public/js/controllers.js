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

            //for each ingredient in recipe,
            //make a restangular call for that ingredient

        })
    })

 .controller('AddRecipeController', function($scope, SessionService, Restangular) {
        $scope.recipe = { ingredients: [] };
        $scope.status = null;
        $scope.methods = [
            { printed_name: 'Bake', stored_name: 'bake' },
            { printed_name: 'Microwave', stored_name: 'microwave' },
            { printed_name: 'Fry', stored_name: 'fry' },
            { printed_name: 'Dutch Oven', stored_name: 'dutch_oven' }];

        Restangular.all('ingredients').getList().then(function(ingredients) {
            $scope.ingredients = ingredients

            for (var ingredientIndex in $scope.ingredients) {
                $scope.ingredients[ingredientIndex].active = true;
            }
        });

        $scope.saveNewRecipe = function() {
            Restangular.all('create-recipe').customPOST($scope.recipe).then(function() {
                $scope.status = "The recipe was successfully created!";
                $scope.recipe = { ingredients: [] };
            }, function() {
                $scope.status = "The recipe couldn't be saved";
            });
        };

        $scope.addIngredient = function(ingredientId) {
            if ($scope.recipe.ingredients.indexOf(ingredientId) == -1) {
                $scope.recipe.ingredients.push(ingredientId);

                for (var ingredientIndex in $scope.ingredients) {
                    var ingredient = $scope.ingredients[ingredientIndex];
                    if (ingredient.id == ingredientId) {
                        $scope.ingredients[ingredientIndex].active = false;
                    }
                }

            }
        }
//adding remove ingredient function
        $scope.removeIngredient = function(ingredientId) {
            var index = $scope.recipe.ingredients.indexOf(ingredientId);
            $scope.recipe.ingredients.splice(index, 1);

            for (var ingredientIndex in $scope.ingredients) {
                var ingredient = $scope.ingredients[ingredientIndex];
                if (ingredient.id == ingredientId) {
                    $scope.ingredients[ingredientIndex].active = true;
                }
            }
        }

        $scope.getIngredientName = function(ingredientId) {
            for (var ingredientIndex in $scope.ingredients) {
                var ingredient = $scope.ingredients[ingredientIndex];
                if (ingredient.id == ingredientId) {
                    return ingredient.name;
                }
            }
        }

        $scope.saveNewRecipe = function(){
            Restangular.all('create-recipe').customPOST($scope.recipe).then(function(){
                $scope.status = 'The recipe was successfully created!';
                $scope.recipe = {};
            }, function(){
                $scope.status = "Sorry, the recipe couldn't be saved";
        })
       }
    })