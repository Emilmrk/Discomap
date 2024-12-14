from django.core.management.base import BaseCommand
from django.core import serializers

class Command(BaseCommand):
    help = 'Load discotecas data from a JSON file'

    def handle(self, *args, **kwargs):
        with open('discotecas.json', 'r') as file:
            data = file.read()
            for obj in serializers.deserialize('json', data):
                obj.save()
        self.stdout.write(self.style.SUCCESS('Successfully loaded discotecas data'))
