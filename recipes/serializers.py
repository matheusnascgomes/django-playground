from rest_framework import serializers
from tag.models import Tag
from .models import Recipe

class TagSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='recipes:tag_api_detail',
        lookup_field='pk'
    )

    class Meta:
        model= Tag
        fields = ['id', 'name', 'slug', 'url']
        

class RecipeSerializer(serializers.Serializer):
    public = serializers.BooleanField(source='is_published')
    preparation = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    tag_object = TagSerializer(many=True, source="tags")

    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
    
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description']

