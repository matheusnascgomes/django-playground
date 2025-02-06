from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer
from tag.models import Tag

class RecipesAPI(ListCreateAPIView):
    """
    API view to retrieve list of recipes or create a new recipe.

    - GET: Returns a list of all recipes.
    - POST: Creates a new recipe.

    Attributes:
        queryset: A queryset containing all Recipe objects.
        serializer_class: The serializer class used to validate and serialize the Recipe objects.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipesItemAPI(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a recipe instance.

    Inherits from:
        RetrieveUpdateDestroyAPIView: A view that provides default implementations for retrieving, updating, and deleting a model instance.

    Attributes:
        queryset (QuerySet): The queryset that should be used for returning objects from this view.
        serializer_class (Serializer): The serializer class that should be used for validating and deserializing input, and for serializing output.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class TagsAPI(ListCreateAPIView):
    """
    API view to retrieve a list of tags or create a new tag.

    This view supports the following actions:
    - GET: Retrieve a list of all tags.
    - POST: Create a new tag.

    Attributes:
        queryset (QuerySet): The queryset that retrieves all Tag objects.
        serializer_class (Serializer): The serializer class used to validate and deserialize input, and serialize output.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagsItemAPI(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a Tag instance.

    This view provides the following actions:
    - Retrieve a single Tag instance by its ID.
    - Update an existing Tag instance.
    - Delete a Tag instance.

    Attributes:
        queryset (QuerySet): The queryset that retrieves all Tag instances.
        serializer_class (Serializer): The serializer class used to validate and deserialize input, and serialize output.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer