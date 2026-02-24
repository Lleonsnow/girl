import uuid
from django.db import models


class CookieConsent(models.Model):
    consent_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, db_index=True)
    consent_type = models.CharField(max_length=20, choices=[('full', 'full'), ('essential', 'essential')])
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=512, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'config_cookieconsent'
        ordering = ['-created_at']
