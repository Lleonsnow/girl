import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        if not username or not password:
            return
        if User.objects.filter(username=username).exists():
            return
        User.objects.create_superuser(username=username, email=email or f'{username}@local', password=password)
        self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created'))
