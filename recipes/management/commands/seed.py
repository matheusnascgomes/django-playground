from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from recipes.models import Category, Recipe
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Popula o banco de dados com categorias e receitas iniciais'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Criando categorias...'))
        categories = ['Café da Manhã', 'Almoço', 'Jantar', 'Sobremesas', 'Lanches']
        category_objects = []
        
        for cat in categories:
            category, created = Category.objects.get_or_create(name=cat)
            category_objects.append(category)
        
        self.stdout.write(self.style.SUCCESS('Categorias criadas!'))
        
        self.stdout.write(self.style.SUCCESS('Criando usuário de teste...'))
        user, created = User.objects.get_or_create(username='admin', defaults={
            'first_name': 'Admin',
            'last_name': 'User',
            'email': 'admin@example.com',
            'is_staff': True,
            'is_superuser': True
        })
        if created:
            user.set_password('admin')
            user.save()
        
        self.stdout.write(self.style.SUCCESS('Usuário criado!'))
        
        self.stdout.write(self.style.SUCCESS('Criando receitas...'))
        recipes = [
            {
                'title': 'Panqueca Americana',
                'description': 'Deliciosa panqueca para o café da manhã.',
                'preparation_time': 15,
                'preparation_time_unit': 'minutos',
                'servings': 2,
                'servings_unit': 'pessoas',
                'preparation_steps': 'Misture os ingredientes e frite em uma frigideira.',
                'is_published': True,
                'category': category_objects[0],
                'author': user
            },
            {
                'title': 'Lasanha de Carne',
                'description': 'Uma lasanha saborosa para o almoço.',
                'preparation_time': 60,
                'preparation_time_unit': 'minutos',
                'servings': 4,
                'servings_unit': 'pessoas',
                'preparation_steps': 'Monte as camadas e leve ao forno.',
                'is_published': True,
                'category': category_objects[1],
                'author': user
            }
        ]
        
        for recipe_data in recipes:
            recipe, created = Recipe.objects.get_or_create(
                title=recipe_data['title'],
                defaults={
                    'description': recipe_data['description'],
                    'slug': slugify(recipe_data['title']),
                    'preparation_time': recipe_data['preparation_time'],
                    'preparation_time_unit': recipe_data['preparation_time_unit'],
                    'servings': recipe_data['servings'],
                    'servings_unit': recipe_data['servings_unit'],
                    'preparation_steps': recipe_data['preparation_steps'],
                    'is_published': recipe_data['is_published'],
                    'category': recipe_data['category'],
                    'author': recipe_data['author'],
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Receitas criadas!'))
