import uuid
from django.db import models


class SiteImage(models.Model):
    CATEGORY_HERO = 'hero'
    CATEGORY_MINIATURE = 'miniature'
    CATEGORY_CAROUSEL = 'carousel'
    CATEGORY_PHOTO = 'photo'
    CATEGORIES = [
        (CATEGORY_HERO, 'Главное фото (герой)'),
        (CATEGORY_MINIATURE, 'Миниатюра CTA'),
        (CATEGORY_CAROUSEL, 'Карусель на главной'),
        (CATEGORY_PHOTO, 'Страница «Фото»'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORIES, db_index=True)
    image = models.ImageField(upload_to='site/%Y/%m/')
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        db_table = 'config_siteimage'
        ordering = ['category', 'order', 'pk']


class CookieConsent(models.Model):
    consent_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, db_index=True)
    consent_type = models.CharField(max_length=20, choices=[('full', 'full'), ('essential', 'essential')])
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=512, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'config_cookieconsent'
        ordering = ['-created_at']
