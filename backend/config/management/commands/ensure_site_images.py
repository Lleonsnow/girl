import os
import re
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand

from config.models import SiteImage


class Command(BaseCommand):
    def handle(self, *args, **options):
        if SiteImage.objects.exists():
            return
        seed_path = Path(os.environ.get('SEED_IMAGES_PATH', '/seed_src'))
        if not seed_path.is_dir():
            return
        created = 0
        hero = seed_path / 'main' / 'main.jpg'
        if hero.is_file():
            with open(hero, 'rb') as f:
                SiteImage.objects.create(category=SiteImage.CATEGORY_HERO, image=File(f, name=hero.name), order=0)
            created += 1
        mini = seed_path / 'main' / 'miniature.jpg'
        if mini.is_file():
            with open(mini, 'rb') as f:
                SiteImage.objects.create(category=SiteImage.CATEGORY_MINIATURE, image=File(f, name=mini.name), order=0)
            created += 1
        carousel_dir = seed_path / 'carousel'
        if carousel_dir.is_dir():
            for i, p in enumerate(sorted(carousel_dir.iterdir(), key=lambda x: _num(x.stem))):
                if p.is_file():
                    with open(p, 'rb') as f:
                        SiteImage.objects.create(category=SiteImage.CATEGORY_CAROUSEL, image=File(f, name=p.name), order=i)
                    created += 1
        photos_dir = seed_path / 'photos'
        if photos_dir.is_dir():
            for i, p in enumerate(sorted(photos_dir.iterdir(), key=lambda x: _num(x.stem))):
                if p.is_file():
                    with open(p, 'rb') as f:
                        SiteImage.objects.create(category=SiteImage.CATEGORY_PHOTO, image=File(f, name=p.name), order=i)
                    created += 1
        if created:
            self.stdout.write(self.style.SUCCESS(f'Seeded {created} site images from {seed_path}'))


def _num(s):
    m = re.match(r'(\d+)', s)
    return int(m.group(1)) if m else 0
