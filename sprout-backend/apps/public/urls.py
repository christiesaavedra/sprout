"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = patterns(
    'apps.public.views',

    url(r'^users$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^recipes$', RecipeList.as_view(), name='recipe-list'),
    url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view(), name='recipe-detail')
)

urlpatterns += patterns('',
	### This endpoint hooks into the REST Framework. We want to extend functionality,
	### So this is commented out and we have defined our own below
	## rul(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
	url(r'^api-token-auth/', ObtainUserAuthToken.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)