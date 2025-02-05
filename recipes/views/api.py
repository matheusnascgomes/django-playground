from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *

from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer
from tag.models import Tag


@api_view(http_method_names=['GET', 'POST'])
def recipe_api_list(request):
    if (request.method == 'GET'):
        recipes = Recipe.objects.get_published()[:10]
        serializer = RecipeSerializer(instance=recipes, many=True, context={'request': request})
        return Response(serializer.data)
    elif (request.method == 'POST'):
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_201_CREATED)

@api_view(http_method_names=['GET', 'PATCH', 'PUT', 'DELETE'])
def recipe_api_detail(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.get_published(),
        pk=pk
    )

    if (request.method == 'GET'):
        serializer = RecipeSerializer(instance=recipe, context={'request': request})
        return Response(serializer.data)
    elif (request.method == 'DELETE'):
        recipe.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    elif (request.method == 'PATCH'):
        serializer = RecipeSerializer(instance=recipe, context={'request': request}, data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_200_OK, data=serializer.data)



@api_view()
def tag_api_detail(request, pk):
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk
    )

    serializer = TagSerializer(
        instance=tag,
        many=False,
        context={'request': request}
    )

    return Response(serializer.data)
