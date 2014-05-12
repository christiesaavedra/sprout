"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf import settings

urlpatterns = patterns(
    'apps.public.views',

    url(r'^users$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)$', UserDetail.as_view(), name='user-detail'),
    # url(r'^home$', Home.as_view(), name='home'),
    url(r'^recipes$', RecipeList.as_view(), name='recipe-list'),
    url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view(), name='recipe-detail'),
    url(r'^create-recipe$', CreateRecipe.as_view(), name='create-recipe'),
    url(r'^ingredients$', IngredientList.as_view(), name='ingredient-list'),
    url(r'^tags$', TagList.as_view(), name='tag-list'),
    url(r'^tags/(?P<pk>[0-9]+)$', TagDetail.as_view(), name='tag-detail'),

    url(r'^getuserid/(?P<token>.+)$', obtain_user_from_token, name='getUserId')

)
urlpatterns += patterns('',
	### This endpoint hooks into the REST Framework. We want to extend functionality,
	### So this is commented out and we have defined our own below
	## rul(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
	url(r'^api-token-auth/', ObtainUserAuthToken.as_view()),

    # serving media files -- debug only
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)