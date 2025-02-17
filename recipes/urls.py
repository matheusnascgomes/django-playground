from django.urls import path, include

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import api, site

app_name = 'recipes'


mvc_routes = [
    ### MVC VIEWS
    path(
        '',
        site.RecipeListViewHome.as_view(),
        name="home"
    ),
    path(
        'recipes/search/',
        site.RecipeListViewSearch.as_view(),
        name="search"
    ),
    path(
        'recipes/tags/<slug:slug>/',
        site.RecipeListViewTag.as_view(),
        name="tag"
    ),
    path(
        'recipes/category/<int:category_id>/',
        site.RecipeListViewCategory.as_view(),
        name="category"
    ),
    path(
        'recipes/<int:pk>/',
        site.RecipeDetail.as_view(),
        name="recipe"
    ),
    path(
        'recipes/api/v1/',
        site.RecipeListViewHomeApi.as_view(),
        name="recipes_api_v1",
    ),
    path(
        'recipes/api/v1/<int:pk>/',
        site.RecipeDetailAPI.as_view(),
        name="recipes_api_v1_detail",
    ),
    path(
        'recipes/theory/',
        site.theory,
        name='theory',
    ),
]

recipes_api_router = SimpleRouter()
tags_api_router = SimpleRouter()

recipes_api_router.register('v2/recipes', api.RecipesViewSet, basename='recipes')
tags_api_router.register('v2/recipes/tags', api.TagsViewSet, basename='tags')


rest_api_routes = [
    path('', include(recipes_api_router.urls)),
    path('', include(tags_api_router.urls)),
    path('v2/recipes/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v2/recipes/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('v2/recipes/token/verify', TokenVerifyView.as_view(), name='token_verify')
]

urlpatterns = mvc_routes + rest_api_routes

