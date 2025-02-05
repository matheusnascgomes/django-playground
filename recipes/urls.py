from django.urls import path

from .views import api, site

app_name = 'recipes'

urlpatterns = [
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
    ### REST API
    path(
        'v2/recipes',
        api.recipe_api_list,
        name='recipes'
    ),
    path(
        'v2/recipes/<int:pk>',
        api.recipe_api_detail,
        name='recipes'
    ),
    path(
        'v2/recipes/tag/<int:pk>',
        api.tag_api_detail,
        name='tag_api_detail'
    )
]
