from rest_framework.status import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer
from tag.models import Tag

class RecipesPagination(PageNumberPagination):
    page_size = 2

class RecipesViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = RecipesPagination

    def get_queryset(self):
        qs = super().get_queryset()

        category_id = self.request.query_params.get('category_id', '')

        if (category_id != '' and category_id.isnumeric()):
            qs = qs.filter(category_id=category_id)

        return qs            
     

class TagsViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
