'use strict';

var sproutApp = angular.module('sproutApp', [
        'ngRoute',
        'restangular',
        'sproutApp.services',
        'sproutApp.controllers',
        'sproutApp.constants',
        'sproutApp.filters',
        'sproutApp.directives',
        'ui.bootstrap'
    ])

    .config(['$routeProvider', 'RestangularProvider', function($routeProvider, RestangularProvider) {
        $routeProvider
            .when('/home', {
                templateUrl: 'partials/home.tpl.html',
                controller: 'HomeController',
                title: 'Home Page'
            })
            .when('/recipes', {
                templateUrl: 'partials/recipes.tpl.html',
                controller: 'RecipesController',
                title: 'Recipes'

            })

            .when('/recipe-details/:recipeId', {
                templateUrl: 'partials/recipe-details.tpl.html',
                controller: 'RecipeDetailsController',
                title: 'Recipe Details'
            })

            .when('/edit-recipe/:recipeId', {
                templateUrl: 'partials/edit-recipe.tpl.html',
                controller: 'EditRecipeController',
                title: 'Edit Recipe'
            })

            .when('/add-recipe', {
                templateUrl: 'partials/add-recipe.tpl.html',
                controller: 'AddRecipeController',
                title: 'Add Recipe'
            })

             .when('/favorites', {
                templateUrl: 'partials/favorites.tpl.html',
                controller: 'FavoritesController',
                title: 'Favorites'
            })

            .otherwise({
                redirectTo: '/recipes'
            });

            RestangularProvider.setBaseUrl('http://localhost:8001');
    }])

    .run(['$location', '$rootScope', 'baseTitle', '$http', 'Restangular', 'SessionService', function ($location, $rootScope, baseTitle, $http, RestangularProvider, SessionService) {
        
        $rootScope.$on('$routeChangeSuccess', function (event, current) {
            // Check to see if the 'title' attribute exists on the route
            if (current.hasOwnProperty('$route')) {
                $rootScope.title = baseTitle + current.$route.title;
            } else {
                $rootScope.title = baseTitle.substring(0, baseTitle.length - 3);
            }
        });

        /* The following is for $http token auth */
        if (SessionService.isLoggedIn()) {
            var token = SessionService.getSession();
            $http.defaults.headers.common['Authorization'] = 'Token ' + token;
        }


        /* add Auth Token to every Restangular request */
        RestangularProvider.setFullRequestInterceptor(function(element, operation, route, url, headers, params) {
            if (SessionService.isLoggedIn()) {
                var token = SessionService.getSession();
                headers['Authorization'] = 'Token ' + token;
            }

            return { element: element, params: params, headers: headers }
        });


    }]);