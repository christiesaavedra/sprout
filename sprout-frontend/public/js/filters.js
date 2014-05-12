'use strict';

/* Filters */

angular.module('sproutApp.filters', [])
    .filter('interpolate', ['version', function (version) {
        return function (text) {
            return String(text).replace(/\%VERSION\%/mg, version);
        }
    }])
    .filter('favoritesFilter', function () {
        return function(recipes, favoriteUser) {
            var favorites = [];

            if (favoriteUser == '') {
                return recipes; // Do not filter.
            }

            for (var i = 0; i < recipes.length; i++) {
                var recipe = recipes[i];

                var favoriteIndex = recipe.favorited_by.indexOf(favoriteUser);

                if (favoriteIndex >= 0) {
                    favorites.push(recipe);
                }
            }

            return favorites;
        }
    });