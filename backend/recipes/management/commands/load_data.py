import json

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Downloading ingredients and tags.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Command start'))
        with open(
            'data/ingredients.json', encoding='utf-8',
        ) as data_file_ingredients:
            ingredient_data = json.loads(data_file_ingredients.read())
            for ingredients in ingredient_data:
                Ingredient.objects.get_or_create(**ingredients)
