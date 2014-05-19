'use strict';

/* Controllers */

angular.module('sproutApp.controllers', [])
    .controller('BaseController', ['$scope', '$window', 'brand', 'SessionService', 'Restangular', function ($scope, $window, brand, SessionService, Restangular) {
        $scope.brand = brand;
        Restangular.all('recipes').getList().then(function (data) {
            $scope.recipes = data;
        });
        $scope.doLogout = function () {
            SessionService.removeSession();
            $window.location = '/';
        };
    }])

    .controller('HomeController', ['$scope', 'SessionService', function ($scope, SessionService) {
        $scope.session = SessionService.getSession();

        $scope.user = {};

        $scope.$on('event:login-confirmed', function () {
            console.log('event has been broadcast to Home Controller');
            $scope.session = SessionService.getSession();
        });
    }])

    .controller('FavoritesController', function ($scope, SessionService, Restangular) {

    })

    .controller('RecipesController', function ($scope, SessionService, Restangular) {

        $scope.session = SessionService.getSession();

        Restangular.one('getuserid', $scope.session).customGET().then(function (data) {
            $scope.userId = parseInt(data);
        })

        Restangular.all('recipes').getList().then(function (data) {
            $scope.recipes = data;
        });

        $scope.ifFavorited = function (recipe) {
            for (var i = 0; i < recipe.favorited_by.length; i++) {
                if ($scope.userId == recipe.favorited_by[i]) {
                    return true;
                }
            }
            return false;
        }

        $scope.favorite = function (recipe) {
            recipe.favorited_by.push($scope.userId);
            Restangular.one('recipes', recipe.id).customPUT(recipe);

        }

        $scope.favoriteUser = '';
        $scope.filterFavorites = function () {
            if ($scope.favoriteUser == $scope.userId) {
                $scope.favoriteUser = '';
            }
            else {
                $scope.favoriteUser = $scope.userId;
            }
        }

        $scope.unfavorite = function (recipe) {
            var index_of_favorite = recipe.favorited_by.indexOf($scope.userId);
            recipe.favorited_by.splice(index_of_favorite, 1);

            Restangular.one('recipes', recipe.id).customPUT(recipe);
        }

    })

    .controller('RecipeDetailsController', function ($scope, SessionService, Restangular, $routeParams) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).customGET().then(function (data) {
            $scope.recipe = data;

        })
    })

    .controller('AddRecipeController', function ($scope, SessionService, Restangular) {
        $scope.recipe = { ingredients: [], tags: [] };
        $scope.status = null;
        $scope.methods = [
            { printed_name: 'Bake', stored_name: 'bake' },
            { printed_name: 'Microwave', stored_name: 'microwave' },
            { printed_name: 'Fry', stored_name: 'fry' },
            { printed_name: 'Dutch Oven', stored_name: 'dutch_oven' }
        ];

        Restangular.all('ingredients').getList().then(function (ingredients) {
            $scope.ingredients = ingredients;

            for (var i = 0; i < $scope.ingredients.length; i++) {
                $scope.ingredients[i].active = true;
            }
        });

        Restangular.all('tags').getList().then(function (tags) {
            $scope.tags = tags;
        });

        $scope.saveNewRecipe = function () {

            $scope.tagObjectsToIds();
            $scope.ingredientObjectsToIds();

            Restangular.all('create-recipe').customPOST($scope.recipe).then(function () {
                $scope.status = "The recipe was successfully created!";
                $scope.recipe = { ingredients: [], tags: [] };
            }, function () {
                $scope.status = "The recipe couldn't be saved";
            });
        };
        $scope.tagObjectsToIds = function () {
            for (var i = 0; i < $scope.recipe.tags.length; i++) {
                var tag = $scope.recipe.tags[i];
                $scope.recipe.tags[i] = tag.id;
            }
        }
        $scope.ingredientObjectsToIds = function () {
            for (var i = 0; i < $scope.recipe.ingredients.length; i++) {
                var tag = $scope.recipe.ingredients[i];
                $scope.recipe.ingredients[i] = ingredient.id;
            }
        }
        $scope.addIngredient = function (ingredientId) {
            if ($scope.recipe.ingredients.indexOf(ingredientId) == -1) {
                $scope.recipe.ingredients.push(ingredientId);

                for (var ingredientIndex in $scope.ingredients) {
                    var ingredient = $scope.ingredients[ingredientIndex];
                    if (ingredient.id == ingredientId) {
                        $scope.ingredients[ingredientIndex].active = false;
                    }
                }

            }
        };

        $scope.removeIngredient = function (ingredientId) {
            var index = $scope.recipe.ingredients.indexOf(ingredientId);
            $scope.recipe.ingredients.splice(index, 1);

            for (var ingredientIndex in $scope.ingredients) {
                var ingredient = $scope.ingredients[ingredientIndex];
                if (ingredient.id == ingredientId) {
                    $scope.ingredients[ingredientIndex].active = true;
                }
            }
        };

        $scope.getIngredientName = function (ingredientId) {
            for (var ingredientIndex in $scope.ingredients) {
                var ingredient = $scope.ingredients[ingredientIndex];
                if (ingredient.id == ingredientId) {
                    return ingredient.name;
                }
            }
        };

        $scope.getTagName = function (tagId) {
            for (var tagIndex in $scope.tags) {
                var tag = $scope.tags[tagIndex];
                if (tag.id == tagId) {
                    return tag.name;
                }
            }
        };

        var getTagFromName = function (tagName) {
            for (var i = 0; i < $scope.tags.length; i++) {
                var tag = $scope.tags[i];
                if (tag.name == tagName) {
                    return tag;
                }
            }
            return null;
        };

        var addTagToRecipe = function (tag) {
            if ($scope.recipe.tags.indexOf(tag) == -1) {
                $scope.recipe.tags.push(tag);
            }
        };

        var createTag = function (tagName) {

            var tag = {name: tagName};
            console.log('Blah' + JSON.stringify(tag))
            Restangular.all('tags').customPOST(tag).then(function (tag) {
                tag.justAdded = true;
                $scope.tags.push(tag);
                addTagToRecipe(tag);
            })
        };

        $scope.saveTag = function (tagName) {
            var tag = getTagFromName(tagName);
            console.log(tag)
            if (tag == null) {
                createTag(tagName);
            }
            else {
                addTagToRecipe(tag);
            }
            $scope.tagName = "";
        };
        //End functions to save tags.

        //Removes the tag from the recipe when the tag's button is clicked //
        $scope.removeTag = function (tag) {
            if (tag.justAdded) {
                //DELETE from server
                Restangular.one('tags', tag.id).customDELETE();
                //DELETE from $scope.tags
                var tagIndex = $scope.tags.indexOf(tag);
                $scope.tags.splice(tagIndex, 1);
            }
            //DELETE from $scope.recipe.tags
            tagIndex = $scope.recipe.tags.indexOf(tag);
            $scope.recipe.tags.splice(tagIndex, 1);

            $scope.tagName = tag.name;
            document.getElementById('tag-input').focus();
        };
        //End functions to delete tags.

        //Functions to save ingredients.
        $scope.saveIngredient = function (ingredientName) {
            console.log('Add ingredient button clicked.' +
                'User typed' + ingredientName);


            //Get ingredient if it already exists.
            var ingredient = getIngredientFromName(ingredientName);
            //Create the ingredient if it doesn't exist.
            if (ingredient == null) {
                createIngredient(ingredientName);
                console.log("You typed a new ingredient!");
            }
            //Add the newly found ingredient to the recipe.
            else {
                addIngredientToRecipe(ingredient);
                console.log("That ingredient already exists!");
            }
            //clear the input box.
            $scope.getIngredientName = '';
        }

        var addIngredientToRecipe = function (ingredient) {
            if ($scope.recipe.ingredients.indexOf(ingredient) == -1) {
                $scope.recipe.ingredients.push(ingredient);
            }
        }
        //new ingredient object that calls the name and glycemic index.
        var createIngredient = function (name) {
            var ingredient = { name: name, glycemic_index: $scope.glycemicIndex};

            Restangular.all('ingredients').customPOST(ingredient).then(function (data) {
                addIngredientToRecipe(data);
            })
        }

        var getIngredientFromName = function (name) {
            for (var i = 0; i < $scope.ingredients.length; i++) {
                var ingredient = $scope.ingredients[i];
                if (ingredient.name == name) {
                    return ingredient;
                }
            }

            return null;
        }
    })


    .controller('EditRecipeController', function ($scope, SessionService, Restangular, $routeParams, $location) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).customGET().then(function (data) {
            $scope.recipe = data;
        })

        $scope.methods = [
            { printed_name: 'Bake', stored_name: 'bake' },
            { printed_name: 'Microwave', stored_name: 'microwave' },
            { printed_name: 'Fry', stored_name: 'fry' },
            { printed_name: 'Dutch Oven', stored_name: 'dutch_oven' }
        ];

        $scope.updateRecipe = function () {
            Restangular.one('recipes', $scope.recipeId).customPUT($scope.recipe).then(function (data) {
                    $scope.status = "The recipe was successfully edited!";
                    $scope.recipe = data;
                    $location.path('/recipes');
                }, function () {
                    $scope.status = "The recipe couldn't be saved";
                }
            )
        }

        $scope.deleteRecipe = function () {
            var response = confirm("Are you sure you want to delete this recipe?");
            if (response == true) {
                Restangular.one('recipes', $scope.recipeId).customDELETE().then(function (data) {
                    $location.path('/recipes');
                }, function () {
                    $scope.status = "The recipe couldn't be deleted";
                });
            }

        }
    })

